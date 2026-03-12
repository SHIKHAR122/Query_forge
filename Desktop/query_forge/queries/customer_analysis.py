from utils.db import QueryEngine

engine = QueryEngine("data/superstore.csv")

def customer_lifetime_value():
    sql = """
        SELECT
            "Customer ID",
            "Customer Name",
            COUNT(DISTINCT "Order ID") AS Total_Orders,
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(SUM(Sales) / COUNT(DISTINCT "Order ID"), 2) AS Avg_Order_Value,
            RANK() OVER(ORDER BY SUM(Sales) DESC) AS Revenue_Rank
        FROM superstore
        GROUP BY "Customer ID", "Customer Name"
        ORDER BY Total_Sales DESC
        LIMIT 20
    """
    return engine.run(sql)



def repeat_vs_onetime_customers():
    sql = """
        WITH customer_orders AS (
            SELECT
                "Customer ID",
                "Customer Name",
                COUNT(DISTINCT "Order ID") AS Total_Orders
            FROM superstore
            GROUP BY "Customer ID", "Customer Name"
        )
        SELECT
            CASE
                WHEN Total_Orders = 1 THEN 'One-Time Customer'
                ELSE 'Repeat Customer'
            END AS Customer_Type,
            COUNT(*) AS Customer_Count,
            ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS Percentage
        FROM customer_orders
        GROUP BY Customer_Type
        ORDER BY Customer_Count DESC
    """
    return engine.run(sql)





def rfm_segmentation():
    sql = """
        WITH rfm AS (
            SELECT
                "Customer ID",
                "Customer Name",
                DATEDIFF('day', MAX(STRPTIME("Order Date", '%m/%d/%Y')), 
                    (SELECT MAX(STRPTIME("Order Date", '%m/%d/%Y')) FROM superstore)) AS Recency,
                COUNT(DISTINCT "Order ID") AS Frequency,
                ROUND(SUM(Sales), 2) AS Monetary
            FROM superstore
            GROUP BY "Customer ID", "Customer Name"
        ),
        rfm_scored AS (
            SELECT
                "Customer ID",
                "Customer Name",
                Recency,
                Frequency,
                Monetary,
                NTILE(5) OVER(ORDER BY Recency ASC) AS R_Score,
                NTILE(5) OVER(ORDER BY Frequency DESC) AS F_Score,
                NTILE(5) OVER(ORDER BY Monetary DESC) AS M_Score
            FROM rfm
        )
        SELECT
            "Customer ID",
            "Customer Name",
            Recency,
            Frequency,
            Monetary,
            R_Score,
            F_Score,
            M_Score,
            (R_Score + F_Score + M_Score) AS RFM_Total_Score,
            CASE
                WHEN (R_Score + F_Score + M_Score) >= 13 THEN 'High Value'
                WHEN (R_Score + F_Score + M_Score) >= 9 THEN 'Medium Value'
                WHEN (R_Score + F_Score + M_Score) >= 6 THEN 'At Risk'
                ELSE 'Low Value'
            END AS Customer_Segment
        FROM rfm_scored
        ORDER BY RFM_Total_Score DESC
    """
    return engine.run(sql)




def customer_revenue_tiers():
    sql = """
        WITH customer_sales AS (
            SELECT
                "Customer ID",
                "Customer Name",
                ROUND(SUM(Sales), 2) AS Total_Sales
            FROM superstore
            GROUP BY "Customer ID", "Customer Name"
        ),
        percentiles AS (
            SELECT
                "Customer ID",
                "Customer Name",
                Total_Sales,
                NTILE(10) OVER(ORDER BY Total_Sales DESC) AS Decile
            FROM customer_sales
        )
        SELECT
            "Customer ID",
            "Customer Name",
            Total_Sales,
            CASE
                WHEN Decile = 1 THEN 'Platinum'
                WHEN Decile = 2 THEN 'Gold'
                WHEN Decile <= 5 THEN 'Silver'
                ELSE 'Bronze'
            END AS Customer_Tier
        FROM percentiles
        ORDER BY Total_Sales DESC
    """
    return engine.run(sql)




def customer_distribution():
    sql = """
        SELECT
            Region,
            Segment,
            COUNT(DISTINCT "Customer ID") AS Total_Customers,
            ROUND(COUNT(DISTINCT "Customer ID") * 100.0 / 
                SUM(COUNT(DISTINCT "Customer ID")) OVER(), 2) AS Customer_Pct
        FROM superstore
        GROUP BY Region, Segment
        ORDER BY Total_Customers DESC
    """
    return engine.run(sql)



def customer_distribution_by_category():
    sql = """
        SELECT
            Category,
            COUNT(DISTINCT "Customer ID") AS Total_Customers,
            ROUND(COUNT(DISTINCT "Customer ID") * 100.0 / 
                SUM(COUNT(DISTINCT "Customer ID")) OVER(), 2) AS Customer_Pct
        FROM superstore
        GROUP BY Category
        ORDER BY Total_Customers DESC
    """
    return engine.run(sql)

def customer_distribution_by_subcategory():
    sql = """
        SELECT
            "Sub-Category",
            COUNT(DISTINCT "Customer ID") AS Total_Customers,
            ROUND(COUNT(DISTINCT "Customer ID") * 100.0 / 
                SUM(COUNT(DISTINCT "Customer ID")) OVER(), 2) AS Customer_Pct
        FROM superstore
        GROUP BY "Sub-Category"
        ORDER BY Total_Customers DESC
    """
    return engine.run(sql)