from utils.db import QueryEngine

engine = QueryEngine("data/superstore.csv")

def monthly_revenue_trend():
    sql = """
        SELECT
            STRFTIME('%Y-%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month,
            ROUND(SUM(Sales), 2) AS Total_Revenue,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct
        FROM superstore
        GROUP BY Month
        ORDER BY Month
    """
    return engine.run(sql)


def mom_growth():
    sql = """
        WITH monthly AS (
            SELECT
                STRFTIME('%Y-%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month,
                ROUND(SUM(Sales), 2) AS Total_Revenue,
                ROUND(SUM(Profit), 2) AS Total_Profit
            FROM superstore
            GROUP BY Month
            ORDER BY Month
        )
        SELECT
            Month,
            Total_Revenue,
            Total_Profit,
            LAG(Total_Revenue) OVER(ORDER BY Month) AS Prev_Month_Revenue,
            ROUND((Total_Revenue - LAG(Total_Revenue) OVER(ORDER BY Month)) / 
                LAG(Total_Revenue) OVER(ORDER BY Month) * 100, 2) AS MoM_Revenue_Growth,
            ROUND((Total_Profit - LAG(Total_Profit) OVER(ORDER BY Month)) / 
                LAG(Total_Profit) OVER(ORDER BY Month) * 100, 2) AS MoM_Profit_Growth
        FROM monthly
        ORDER BY Month
    """
    return engine.run(sql)



def yoy_comparison():
    sql = """
        WITH yearly AS (
            SELECT
                STRFTIME('%Y', STRPTIME("Order Date", '%m/%d/%Y')) AS Year,
                STRFTIME('%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month_Num,
                ROUND(SUM(Sales), 2) AS Total_Revenue
            FROM superstore
            GROUP BY Year, Month_Num
        )
        SELECT
            Month_Num,
            SUM(CASE WHEN Year = '2014' THEN Total_Revenue ELSE 0 END) AS Revenue_2014,
            SUM(CASE WHEN Year = '2015' THEN Total_Revenue ELSE 0 END) AS Revenue_2015,
            SUM(CASE WHEN Year = '2016' THEN Total_Revenue ELSE 0 END) AS Revenue_2016,
            SUM(CASE WHEN Year = '2017' THEN Total_Revenue ELSE 0 END) AS Revenue_2017
        FROM yearly
        GROUP BY Month_Num
        ORDER BY Month_Num
    """
    return engine.run(sql)


def cumulative_revenue():
    sql = """
        WITH monthly AS (
            SELECT
                STRFTIME('%Y-%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month,
                ROUND(SUM(Sales), 2) AS Total_Revenue
            FROM superstore
            GROUP BY Month
        )
        SELECT
            Month,
            Total_Revenue,
            ROUND(SUM(Total_Revenue) OVER(ORDER BY Month), 2) AS Cumulative_Revenue,
            ROUND(SUM(Total_Revenue) OVER(ORDER BY Month) / 
                SUM(Total_Revenue) OVER() * 100, 2) AS Cumulative_Pct
        FROM monthly
        ORDER BY Month
    """
    return engine.run(sql)


def rolling_revenue_trend():
    sql = """
        WITH monthly AS (
            SELECT
                STRFTIME('%Y-%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month,
                ROUND(SUM(Sales), 2) AS Total_Revenue
            FROM superstore
            GROUP BY Month
        )
        SELECT
            Month,
            Total_Revenue,
            ROUND(AVG(Total_Revenue) OVER(
                ORDER BY Month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
            ), 2) AS Rolling_3Month_Avg,
            ROUND(AVG(Total_Revenue) OVER(
                ORDER BY Month ROWS BETWEEN 5 PRECEDING AND CURRENT ROW
            ), 2) AS Rolling_6Month_Avg
        FROM monthly
        ORDER BY Month
    """
    return engine.run(sql)


def sales_volatility():
    sql = """
        WITH monthly AS (
            SELECT
                STRFTIME('%Y-%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month,
                ROUND(SUM(Sales), 2) AS Total_Revenue
            FROM superstore
            GROUP BY Month
        ),
        stats AS (
            SELECT
                Month,
                Total_Revenue,
                AVG(Total_Revenue) OVER() AS Avg_Revenue,
                STDDEV(Total_Revenue) OVER() AS Stddev_Revenue
            FROM monthly
        )
        SELECT
            Month,
            Total_Revenue,
            ROUND(Avg_Revenue, 2) AS Avg_Revenue,
            ROUND(Stddev_Revenue, 2) AS Stddev_Revenue,
            ROUND((Total_Revenue - Avg_Revenue) / Stddev_Revenue, 2) AS Z_Score,
            CASE
                WHEN ABS((Total_Revenue - Avg_Revenue) / Stddev_Revenue) > 2 THEN 'Anomaly'
                WHEN ABS((Total_Revenue - Avg_Revenue) / Stddev_Revenue) > 1 THEN 'Unusual'
                ELSE 'Normal'
            END AS Volatility_Tag
        FROM stats
        ORDER BY Month
    """
    return engine.run(sql)