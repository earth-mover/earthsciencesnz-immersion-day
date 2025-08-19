# earthsciencesnz-immersion-day

## Workshop Description

Welcome to the Earth Sciences New Zealand Immersion Day! This hands-on workshop demonstrates how to go "From Unified Data to Insight: Building a Cross-Organizational Weather Application" in just a few hours.

### What You'll Learn

As a Earth Sciences New Zealand participant, you'll experience firsthand how modern cloud-native data tools can transform your workflow:

- **Discover and Access Data**: Learn how Earthmover's data catalog makes vast datasets easily discoverable and instantly accessible, eliminating the usual data wrangling bottlenecks
- **Accelerated Analysis**: Experience the speed of performing complex analyses on large geospatial datasets using Xarray and Icechunk - what used to take hours now takes minutes
- **Cross-Organizational Collaboration**: See how data from different sources can be seamlessly combined to create new insights and data products
- **Rapid Application Development**: Build a complete web application with interactive maps that queries live data - from concept to deployment in a single session

### What You'll Build

By the end of this workshop, you'll have:
1. Explored a comprehensive weather and climate data catalog
2. Performed real-world analysis on New Zealand climate data
3. Created a new derived data product by fusing multiple datasets
4. Built an interactive web map application that serves your analysis

This workshop demonstrates how the combined NIWA/MetService organizations can leverage modern data infrastructure to accelerate research, improve operational efficiency, and deliver better services to New Zealand.

## AWS Specifics

- **AWS region**: `us-east-1`
- **AWS services required**: 
  - SageMaker
  - Standard S3 Bucket + [IAM Role](https://docs.earthmover.io/setup/manage-storage#aws-s3-buckets)
- **Notebook requirements**: See [requirements.txt](./requirements.txt)
- **AWS infrastructure requirements**: `ml.m5.4xlarge` (16 cpu, 64gb ram) or larger

## Key Links

- **Proposed agenda** → https://docs.google.com/document/d/1gz9Su0TViXZ61EX1MaYTU8IVQ8mz-uDDpDS8bhK7npQ/edit?tab=t.0
- **Arraylake Org** → https://app.earthmover.io/earthsciencesnz
- **Workshop GitHub Repo** → https://github.com/earth-mover/earthsciencesnz-immersion-day

## Workshop Agenda

**Theme**: From Unified Data to Insight: Building a Cross-Organizational Weather Application

### Learning Objectives
- Understand how Earthmover's components (Arraylake catalog, Icechunk, Xarray, Zarr, and Flux) create a high-performance, scalable platform for interacting with geospatial Earth system data and for building data applications and products
- Experience the speed and simplicity of performing analysis on large datasets using Xarray and Icechunk in a native Python environment
- Create and share a new, derived data product that can be used in a dashboard-style application via the Flux API

### Proposed Schedule

#### Intro / Core Challenge
Your organizations have vast and valuable datasets. The goal is to make them easily discoverable, combinable, and accessible for rapid product development. Today, we'll show you how.

Explaining how Earthmover's combination of open source tools and open-core platform provides a managed, performant layer that eliminates infrastructure headaches and accelerates data product delivery.

Clarify the catalog technology, differentiating it from a simple STAC implementation by highlighting its performance and governance features.

#### Lab 0: Getting Started with Xarray and Zarr
Users will learn the basic concepts behind Xarray and Zarr, and how to use them to access and query large datasets.

#### Lab 1: Exploring the Catalog - "Discover what's available"
Users log into a pre-configured AWS SageMaker Studio environment and explore the pre-loaded data catalog (ERA5, DEM, etc.) in a Jupyter Notebook.

Run basic Xarray queries that are accelerated by Icechunk, experiencing the platform's speed firsthand.

#### Lab 2: Initial Analysis - "Let's answer a real question"
Guide users to perform a relevant analysis task, like calculating a fire-weather index for a specific NZ region or identifying areas that have experienced anomalous rainfall. This provides an early, tangible win.

#### Lab 3: Creating a New Data Product
Create something new by fusing data across domains—the core vision of the merger.

Guide users through a more advanced workflow that combines multiple datasets (e.g., elevation data from the DEM and rainfall data from ERA5).

They will create a new, derived dataset—for example, a "Landslide Susceptibility Index"—and write it back into the Earthmover platform, making it a new, reusable asset.

#### Lab 4: Building a Slippy Map
Users build a simple, interactive WMS slippy tile map in Mapbox that makes live queries to the new data product via Earthmover's Flux API, demonstrating a complete "data-to-decision" workflow.

#### Wrap-up & Next Steps
**Narrative**: "Today, you went from raw data to a functioning application in a few hours. Let's discuss how this approach can accelerate your most important projects."

Review the day's accomplishments, discuss scalability architecture, and open the floor for Q&A.
