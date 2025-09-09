# Lab 1: Catalog Exploration and Interaction

**Duration**: 50 minutes
**Presenter**: Tom Nichols (Earthmover)

## Overview

In this lab, you'll explore the Earthmover data catalog to discover what datasets are available and how to access them. You'll log into the [Arraylake application](https://app.earthmover.io) and your pre-configured AWS SageMaker Studio environment to interact with large climate datasets in real-time.

## Learning Objectives

By the end of this lab, you will:

- Navigate the Arraylake data catalog interface
- Understand what datasets are available (ERA5, DEM, etc.)
- Access datasets directly in your Jupyter environment
- Run Xarray queries that are accelerated by Icechunk
- Experience the platform's speed when working with large datasets
- Understand the difference between traditional data access and Earthmover's approach

## Key Datasets You'll Explore

- **ERA5 Reanalysis**: Comprehensive atmospheric reanalysis data
- **Digital Elevation Model (DEM)**: High-resolution topographic data
- **Additional climate datasets**: Temperature, precipitation, wind patterns

## What You'll Do

1. **Catalog Navigation**: Browse available datasets in the Arraylake interface
2. **Dataset Discovery**: Examine metadata, coverage, and resolution for each dataset
3. **Direct Access**: Connect to datasets from your Jupyter notebook
4. **Speed Test**: Experience Icechunk-accelerated queries on large datasets
5. **Basic Queries**: Select data for New Zealand regions and specific time periods
6. **Performance Comparison**: See how fast you can access TB-scale datasets

## Key Technologies

- **Arraylake Catalog**: Organized, governed access to datasets
- **Icechunk**: High-performance chunked data access
- **Zarr**: Cloud-native array storage format
- **Xarray**: Python toolkit for labeled arrays and datasets

This lab demonstrates how Earthmover eliminates the usual "data download and wait" bottlenecks that slow down climate research.
