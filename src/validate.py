import logging

def validate_sales_data(df):

    if df["order_id"].isnull().sum() > 0:
        logging.warning("Missing order_id values detected")

    if df["customer_id"].isnull().sum() > 0:
        logging.warning("Missing customer_id values detected")

    if (df["quantity"] <= 0).any():
        logging.warning("Invalid quantity values detected")

        