# Lab 2: Studying Anomalous Rainfall

**Duration**: 50 minutes
**Presenter**: Deepak Cherian (Earthmover)

## Overview

Study rainfall patterns and anomalies using ERA5 precipitation data over New Zealand. This lab demonstrates "typical" climatology statistics and comparisons to observational data, showing how quickly you can go from research question to meaningful results.

## Learning Objectives

By the end of this lab, you will:

- Use Xarray's high-level API (groupby, resample) for expressive climate computations
- Calculate monthly climatologies and precipitation anomalies
- Compare ERA5 reanalysis data with Met Station observations
- Create time series plots and spatial correlation maps
- Experience fast analysis on multi-TB datasets

## What You'll Do

1. **Subset ERA5 data** to New Zealand and calculate total precipitation
2. **Monthly climatology** - group by month and calculate long-term averages
3. **Anomaly analysis** - compute deviations from monthly climatology
4. **Resampling** - convert to monthly frequency and smooth time series
5. **Data comparison** - correlate ERA5 with Met Station observations
6. **Spatial analysis** - interpolate model data to station locations and visualize correlations

## Key Techniques

- **GroupBy operations**: `groupby("time.month")` for climatology calculations
- **Anomaly calculations**: Subtracting group means from original data
- **Resampling**: `resample(time="MS")` for frequency conversion
- **Data alignment**: `xr.align()` and `interp()` for comparing datasets
- **Correlation analysis**: `xr.corr()` for model-observation comparisons

## Expected Outcome

A complete rainfall analysis workflow demonstrating how Xarray's computational patterns enable rapid climate research on large datasets.

## Further Reading

1. [Icechunk Documentation](https://icechunk.io/en/latest/overview/)
1. [Earthmover Documentation](https://docs.earthmover.io/)
