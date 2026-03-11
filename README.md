# Sales Data ETL Pipeline using Python & Pandas

## Project Overview

This project simulates a simple **data engineering ETL pipeline** that processes raw sales data from multiple datasets and generates business reports.

The pipeline performs the following steps:

1. Extract raw CSV datasets
2. Validate input data
3. Clean and transform the data
4. Merge datasets
5. Generate aggregated reports
6. Export processed datasets

---

## Technologies Used

* Python
* Pandas
* CSV datasets

---

## Project Structure

sales-data-etl-pipeline/

data/
    sales.csv
    customers.csv
    products.csv

src/
    extract.py
    transform.py
    validate.py
    load.py
    pipeline.py

output/
    revenue_by_region.csv
    monthly_revenue.csv
    top_products.csv

logs/
    pipeline.log

notebooks/
    exploration.ipynb

---

## Pipeline Steps

### 1. Data Extraction

Raw datasets are loaded using Pandas.

### 2. Data Validation

Basic checks ensure that key fields are not missing and values are valid.

### 3. Data Cleaning

Duplicates are removed and missing values are handled.

### 4. Data Transformation

New features such as **revenue** and **month** are created.

### 5. Data Aggregation

The pipeline generates summary reports including:

* Revenue by region
* Monthly revenue
* Top selling products

### 6. Data Export

Processed reports are saved to the `output` directory.

---

## How to Run the Pipeline

Navigate to the project directory:

```
cd sales-data-etl-pipeline
```

Run the pipeline:

```
python src/pipeline.py
```

---

## Example Outputs

The pipeline generates:

* revenue_by_region.csv
* monthly_revenue.csv
* top_products.csv

---

## Author

Data Engineering practice project using Python and Pandas.
