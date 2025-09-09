# Lab 3: Build a Landslide Susceptibility Index

**Duration**: 60 minutes
**Presenter**: [Joe Hamman](https://github.com/jhamman) (Earthmover)

## Overview

Combine elevation data from Copernicus DEM with ERA5 precipitation data to create a Landslide Susceptibility Index. This lab demonstrates data fusion workflows and how to create new, reusable data products in the Earthmover platform.

## Learning Objectives

By the end of this lab, you will:

- Combine datasets from different domains (topography + weather)
- Calculate slope gradients from elevation data
- Process daily precipitation with rolling windows
- Interpolate between different spatial grids
- Write new datasets back to the Arraylake catalog
- Experience the full cycle from raw data to new data product

## What You'll Build

A **Landslide Susceptibility Index** that combines:
- **Copernicus DEM**: 90m resolution elevation data for New Zealand
- **ERA5 precipitation**: Daily rainfall with 7-day rolling accumulation
- **Slope calculation**: Derived from elevation gradients
- **Custom landslide model**: Using provided `landslide` module functions

## Key Workflow Steps

1. **Load input datasets** - Access DEM and ERA5 data from Arraylake
2. **Calculate slope** - Derive slope gradients from elevation using `calculate_slope()`
3. **Process precipitation** - Create daily totals and 7-day rolling accumulation
4. **Spatial interpolation** - Resample ERA5 to 90m DEM grid resolution
5. **Calculate index** - Apply landslide susceptibility model using `landslide_index()`
6. **Create repository** - Set up new Arraylake repo with metadata
7. **Write data** - Save results using Icechunk and commit changes

## Technical Skills

- **Multi-resolution data fusion**: Combining 25km ERA5 with 90m DEM data
- **Temporal processing**: Daily resampling and rolling window operations
- **Spatial interpolation**: Grid-to-grid resampling with `interp()`
- **Custom scientific functions**: Using domain-specific landslide calculations
- **Data publishing**: Creating repos, writing with Zarr, and committing with Icechunk

## Expected Outcome

A new Landslide Susceptibility Index dataset in your personal Arraylake repository, demonstrating how to create valuable derived products from multiple data sources.
