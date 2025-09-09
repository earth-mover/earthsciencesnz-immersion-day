import dask.array as da
import numpy as np
import xarray as xr


def calculate_slope(
    dem: xr.DataArray, dx: float = None, dy: float = None
) -> xr.DataArray:
    """
    Calculate slope (in degrees) from a DEM using central differences.
    Supports Dask arrays with map_overlap for parallel computation.

    Parameters
    ----------
    dem : xr.DataArray
        Elevation in meters (can be chunked with Dask).
    dx : float, optional
        Grid spacing in x-direction (same units as DEM coordinates).
        If None, inferred from dem.x.
    dy : float, optional
        Grid spacing in y-direction (same units as DEM coordinates).
        If None, inferred from dem.y.

    Returns
    -------
    slope : xr.DataArray
        Slope in degrees.
    """
    if dx is None:
        raise ValueError("dx is required")
    if dy is None:
        raise ValueError("dy is required")

    def gradient_block(block):
        dz_dy, dz_dx = np.gradient(block, dy, dx)
        slope_rad = np.arctan(np.sqrt(dz_dx**2 + dz_dy**2))
        return np.degrees(slope_rad)

    if isinstance(dem.data, da.Array):
        # Use map_overlap for chunked Dask arrays
        slope_data = dem.data.map_overlap(
            gradient_block,
            depth=1,  # 1 cell overlap for central differences
            boundary="reflect",
            dtype=dem.dtype,
        )
    else:
        slope_data = gradient_block(dem.values)

    return xr.DataArray(slope_data, coords=dem.coords, dims=dem.dims, name="slope")


def landslide_index(
    dem: xr.DataArray, precip: xr.DataArray, dx: float = None, dy: float = None
) -> xr.DataArray:
    """
    Compute a simple landslide susceptibility index based on slope and precipitation.

    Parameters
    ----------
    dem : xr.DataArray
        DEM elevation in meters.
    precip : xr.DataArray
        Accumulated precipitation (e.g., 7-day total in mm).

    Returns
    -------
    index : xr.DataArray
        Normalized landslide susceptibility index [0-1].
    """
    slope = calculate_slope(dem, dx=dx, dy=dy)

    # Normalize slope and precip to 0–1
    slope_norm = (slope - slope.min()) / (slope.max() - slope.min())
    precip_norm = (precip - precip.min()) / (precip.max() - precip.min())

    index = slope_norm * precip_norm
    index.name = "landslide_index"
    return index
