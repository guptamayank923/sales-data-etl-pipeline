import pandas as pd
import logging

def clean_sales_data(df):

    df = df.drop_duplicates()

    df = df.dropna(subset=["customer_id","product_id"])

    df["quantity"] = df["quantity"].fillna(1)

    df["order_date"] = pd.to_datetime(df["order_date"])

    logging.info("Sales dataset cleaned")

    return df

def merge_datasets(sales, customers, products):

    merged = sales.merge(customers, on="customer_id")

    merged = merged.merge(products, on="product_id")

    logging.info("Datasets merged successfully")

    return merged


def transform_data(df):

    df["revenue"] = df["quantity"] * df["price"]

    df["month"] = df["order_date"].dt.to_period("M")

    logging.info("Revenue and month columns created")

    return df

def generate_reports(df):

    revenue_region = df.groupby("region")["revenue"].sum()

    monthly_revenue = df.groupby("month")["revenue"].sum()

    top_products = (
        df.groupby("product_name")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    return revenue_region, monthly_revenue, top_products