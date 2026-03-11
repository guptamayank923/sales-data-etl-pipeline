import pandas as pd
import logging

def load_sales_data(path):
    logging.info("Loading sales dataset")
    return pd.read_csv(path)

def load_customers_data(path):
    logging.info("Loading customers dataset")
    return pd.read_csv(path)

def load_products_data(path):
    logging.info("Loading products dataset")
    return pd.read_csv(path)