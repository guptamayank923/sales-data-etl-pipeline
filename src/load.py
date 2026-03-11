import logging

def export_reports(region, monthly, top_products):

    region.to_csv("output/revenue_by_region.csv")

    monthly.to_csv("output/monthly_revenue.csv")

    top_products.to_csv("output/top_products.csv")

    logging.info("Reports exported successfully")