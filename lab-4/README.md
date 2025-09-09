# Lab 4: Data Access through Flux

**Duration**: 60 minutes
**Presenter**: [Deepak Cherian](https://github.com/dcherian) (Earthmover)

## Overview

Explore how to access your data through standard Web APIs using **Flux** - Earthmover's Data Delivery service. This lab demonstrates how to bridge the gap between new technologies (Zarr/Icechunk/Arraylake) and legacy workflows by making data accessible in various standard formats.

## Learning Objectives

By the end of this lab, you will:

- Access Arraylake data through standard Web APIs without using the Arraylake Client
- Export data to tabular formats (CSV) for use in spreadsheets and traditional tools
- Serve map tiles for web mapping applications
- Use OPeNDAP protocol to access data with standard NetCDF tools
- Understand how Flux enables interoperability with existing workflows

## What You'll Explore

### 1. Tabular Data Access (EDR API)
- **Export to CSV**: Use pandas to read data directly from Flux URLs
- **Google Sheets integration**: Import data using `IMPORTDATA()` function
- **Excel compatibility**: Test data access in Microsoft Excel
- **Time series extraction**: Get data for specific locations and time ranges

### 2. Map Tile Services
- **Web mapping**: Integrate data as tile layers using ipyleaflet
- **MapBox integration**: Simple HTML examples with live data tiles
- **Standard protocols**: OGC Tiles API for interoperability
- **Real-time visualization**: Dynamic map tiles with custom styling

### 3. OPeNDAP Integration
- **NetCDF tools**: Access data using `ncdump`, `ncview`, and other standard tools
- **Legacy workflow support**: Enable existing analysis pipelines
- **Metadata exploration**: Examine data structure without downloading

## Key Flux Services

- **EDR API**: Environmental Data Retrieval for point/area queries
- **Tiles Service**: OGC-compliant map tiles (WebMercatorQuad)
- **OPeNDAP**: Network Common Data Form access protocol
- **Multiple formats**: CSV, JSON, NetCDF, PNG tiles

## Technical Skills

- **URL construction**: Building Flux API endpoints with proper parameters
- **Web integration**: Adding live data to web mapping applications
- **Format conversion**: Accessing the same data in multiple output formats
- **Standard protocols**: Using OGC and OPeNDAP standards for interoperability

## Expected Outcome

Understanding how Flux makes your Arraylake data accessible through standard Web APIs, enabling integration with existing tools, workflows, and applications without requiring specialized knowledge of Zarr or Icechunk.

**Key insight**: Data must be accessible to be useful - Flux bridges new technologies with established workflows.
