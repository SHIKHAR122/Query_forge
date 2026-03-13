import time
from utils.db import QueryEngine
from queries.sales_analysis import (
    total_sales_by_region, sales_rank_by_region,
    sales_vs_profit_by_region, sales_by_category,
    subcategory_performance, sales_by_segment,
    monthly_sales_trend, yoy_growth,
    highest_lowest_sales_month, seasonal_patterns,
    pareto_analysis
)
from queries.customer_analysis import (
    customer_lifetime_value, repeat_vs_onetime_customers,
    rfm_segmentation, customer_revenue_tiers,
    customer_distribution, customer_distribution_by_category,
    customer_distribution_by_subcategory
)
from queries.product_analysis import (
    best_selling_products, most_profitable_products,
    negative_margin_products, product_profit_margin_analysis,
    product_pareto_analysis
)
from queries.time_series_analysis import (
    monthly_revenue_trend, mom_growth,
    yoy_comparison, cumulative_revenue,
    rolling_revenue_trend, sales_volatility
)

def benchmark_all_queries():
    queries = {
        "total_sales_by_region": total_sales_by_region,
        "sales_rank_by_region": sales_rank_by_region,
        "sales_vs_profit_by_region": sales_vs_profit_by_region,
        "sales_by_category": sales_by_category,
        "subcategory_performance": subcategory_performance,
        "sales_by_segment": sales_by_segment,
        "monthly_sales_trend": monthly_sales_trend,
        "yoy_growth": yoy_growth,
        "highest_lowest_sales_month": highest_lowest_sales_month,
        "seasonal_patterns": seasonal_patterns,
        "pareto_analysis": pareto_analysis,
        "customer_lifetime_value": customer_lifetime_value,
        "repeat_vs_onetime_customers": repeat_vs_onetime_customers,
        "rfm_segmentation": rfm_segmentation,
        "customer_revenue_tiers": customer_revenue_tiers,
        "customer_distribution": customer_distribution,
        "customer_distribution_by_category": customer_distribution_by_category,
        "customer_distribution_by_subcategory": customer_distribution_by_subcategory,
        "best_selling_products": best_selling_products,
        "most_profitable_products": most_profitable_products,
        "negative_margin_products": negative_margin_products,
        "product_profit_margin_analysis": product_profit_margin_analysis,
        "product_pareto_analysis": product_pareto_analysis,
        "monthly_revenue_trend": monthly_revenue_trend,
        "mom_growth": mom_growth,
        "yoy_comparison": yoy_comparison,
        "cumulative_revenue": cumulative_revenue,
        "rolling_revenue_trend": rolling_revenue_trend,
        "sales_volatility": sales_volatility
    }

    results = []
    for name, func in queries.items():
        start = time.time()
        func()
        end = time.time()
        execution_time = round(end - start, 4)
        results.append({
            "Query": name,
            "Execution_Time_Seconds": execution_time,
            "Performance": "Fast" if execution_time < 0.1 else "Moderate" if execution_time < 0.5 else "Slow"
        })

    import pandas as pd
    return pd.DataFrame(results).sort_values("Execution_Time_Seconds", ascending=False)