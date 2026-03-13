# Sales Data ETL and Analytics Pipeline

## Project Overview
This project implements a complete data engineering and analytics pipeline. It covers the entire lifecycle of sales data, including raw data ingestion, SQL-based transformation, and Machine Learning forecasting.

## Repository Structure and Files
* Python_Script/
    * ingest_raw_dataset.py: Script for initial data ingestion.
    * ingest_clean_dataset.py: Logic for automated data cleaning and preprocessing.
    * Sales_Model_Training.py: Machine Learning model implementation and training.
    * visualize_results.py: Script for generating analytical charts.
    * model_performance_report.png: Visual representation of model metrics.
* SQL_Script/
    * etl_sales_cleaning.sql: SQL procedures for data transformation.
* Sales Dataset/
    * project1_sales.csv: The original raw dataset.
    * clean_sales_dataset.csv: The final processed dataset.
* Reports/
    * Sales_Analysis_Report.docx: Comprehensive documentation of business insights.

## Tech Stack
* Language: Python (Pandas, Scikit-learn, Matplotlib)
* Database: SQL (Transformation and Data Integrity)
* Methodology: ETL (Extract, Transform, Load) and Predictive Analytics

## Execution Workflow
1. Data Ingestion: Run scripts to import raw data.
2. Data Cleaning: Execute the SQL script or the Python cleaning script for normalization.
3. Analysis: Run the training script to generate sales forecasts and performance reports.
