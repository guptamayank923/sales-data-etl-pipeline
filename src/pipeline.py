import logging

# Setup logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Import pipeline modules
from extract import load_sales_data, load_customers_data, load_products_data
from validate import validate_sales_data
from transform import clean_sales_data, merge_datasets, transform_data, generate_reports
from load import export_reports


def run_pipeline():

    logging.info("Pipeline started")

    # Extract
    sales = load_sales_data("data/sales.csv")
    customers = load_customers_data("data/customers.csv")
    products = load_products_data("data/products.csv")

    # Validate
    validate_sales_data(sales)

    # Clean
    sales = clean_sales_data(sales)

    # Merge
    df = merge_datasets(sales, customers, products)

    # Transform
    df = transform_data(df)

    # Generate reports
    region, monthly, top_products = generate_reports(df)

    # Export
    export_reports(region, monthly, top_products)

    logging.info("Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()