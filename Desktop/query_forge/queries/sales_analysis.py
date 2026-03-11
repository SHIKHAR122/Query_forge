from utils.db import QueryEngine

engine = QueryEngine("data/superstore.csv")

def total_sales_by_region():
    sql = """
        SELECT 
            Region,
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct,
            ROUND(SUM(Sales) / SUM(SUM(Sales)) OVER() * 100, 2) AS Revenue_Contribution_Pct,
            RANK() OVER(ORDER BY SUM(Sales) DESC) AS Sales_Rank
        FROM superstore
        GROUP BY Region
        ORDER BY Total_Sales DESC
    """
    return engine.run(sql)



def sales_rank_by_region():
    sql = """
        SELECT
            Region,
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            RANK() OVER(ORDER BY SUM(Sales) DESC) AS Sales_Rank,
            RANK() OVER(ORDER BY SUM(Profit) DESC) AS Profit_Rank,
            CASE 
                WHEN RANK() OVER(ORDER BY SUM(Sales) DESC) = 1 THEN 'Highest Performing'
                WHEN RANK() OVER(ORDER BY SUM(Sales) DESC) = 4 THEN 'Lowest Performing'
                ELSE 'Mid Tier'
            END AS Performance_Tag
        FROM superstore
        GROUP BY Region
        ORDER BY Sales_Rank
    """
    return engine.run(sql)




def sales_vs_profit_by_region():
    sql = """
        SELECT
            Region,
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            CASE
                WHEN SUM(Profit) / SUM(Sales) * 100 < 10 THEN 'Low Margin — Investigate'
                WHEN SUM(Profit) / SUM(Sales) * 100 BETWEEN 10 AND 15 THEN 'Moderate Margin'
                ELSE 'Healthy Margin'
            END AS Margin_Health
        FROM superstore
        GROUP BY Region
        ORDER BY Total_Sales DESC
    """
    return engine.run(sql)



def sales_by_category():
    sql = """
        SELECT
            Category,
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct,
            ROUND(SUM(Sales) / SUM(SUM(Sales)) OVER() * 100, 2) AS Revenue_Contribution_Pct,
            RANK() OVER(ORDER BY SUM(Sales) DESC) AS Revenue_Rank,
            RANK() OVER(ORDER BY SUM(Profit) DESC) AS Profit_Rank,
            CASE
                WHEN SUM(Sales) > 500000 AND SUM(Profit) / SUM(Sales) * 100 < 10 
                    THEN 'High Sales Low Margin — Risk'
                ELSE 'Normal'
            END AS Risk_Flag
        FROM superstore
        GROUP BY Category
        ORDER BY Total_Sales DESC
    """
    return engine.run(sql)




def subcategory_performance():
    sql = """
        SELECT
            Category,
            "Sub-Category",
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct,
            RANK() OVER(PARTITION BY Category ORDER BY SUM(Sales) DESC) AS Rank_Within_Category,
            CASE
                WHEN SUM(Profit) < 0 THEN 'Loss Making'
                WHEN SUM(Profit) / SUM(Sales) * 100 < 5 THEN 'Low Margin'
                ELSE 'Healthy'
            END AS Health_Status
        FROM superstore
        GROUP BY Category, "Sub-Category"
        ORDER BY Category, Total_Sales DESC
    """
    return engine.run(sql)




def sales_by_segment():
    sql = """
        SELECT
            Segment,
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct,
            ROUND(SUM(Sales) / SUM(SUM(Sales)) OVER() * 100, 2) AS Revenue_Contribution_Pct,
            ROUND(SUM(Sales) / COUNT(DISTINCT "Order ID"), 2) AS Avg_Order_Value,
            RANK() OVER(ORDER BY SUM(Sales) DESC) AS Revenue_Rank,
            RANK() OVER(ORDER BY SUM(Profit) DESC) AS Profit_Rank
        FROM superstore
        GROUP BY Segment
        ORDER BY Total_Sales DESC
    """
    return engine.run(sql)





def monthly_sales_trend():
    sql = """
        WITH monthly AS (
            SELECT
                STRFTIME('%Y-%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month,
                ROUND(SUM(Sales), 2) AS Total_Sales,
                ROUND(SUM(Profit), 2) AS Total_Profit
            FROM superstore
            GROUP BY Month
            ORDER BY Month
        )
        SELECT
            Month,
            Total_Sales,
            Total_Profit,
            ROUND(SUM(Total_Sales) OVER(ORDER BY Month), 2) AS Cumulative_Sales,
            ROUND(AVG(Total_Sales) OVER(ORDER BY Month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS Rolling_3Month_Avg,
            ROUND((Total_Sales - LAG(Total_Sales) OVER(ORDER BY Month)) / LAG(Total_Sales) OVER(ORDER BY Month) * 100, 2) AS MoM_Growth_Pct
        FROM monthly
        ORDER BY Month
    """
    return engine.run(sql)




def yoy_growth():
    sql = """
        WITH yearly AS (
            SELECT
                STRFTIME('%Y', STRPTIME("Order Date", '%m/%d/%Y')) AS Year,
                ROUND(SUM(Sales), 2) AS Total_Sales,
                ROUND(SUM(Profit), 2) AS Total_Profit
            FROM superstore
            GROUP BY Year
            ORDER BY Year
        )
        SELECT
            Year,
            Total_Sales,
            Total_Profit,
            LAG(Total_Sales) OVER(ORDER BY Year) AS Previous_Year_Sales,
            ROUND((Total_Sales - LAG(Total_Sales) OVER(ORDER BY Year)) / LAG(Total_Sales) OVER(ORDER BY Year) * 100, 2) AS YoY_Growth_Pct
        FROM yearly
        ORDER BY Year
    """
    return engine.run(sql)





def highest_lowest_sales_month():
    sql = """
        WITH monthly AS (
            SELECT
                STRFTIME('%Y-%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month,
                ROUND(SUM(Sales), 2) AS Total_Sales
            FROM superstore
            GROUP BY Month
        )
        SELECT
            Month,
            Total_Sales,
            CASE
                WHEN Total_Sales = MAX(Total_Sales) OVER() THEN 'Highest Sales Month'
                WHEN Total_Sales = MIN(Total_Sales) OVER() THEN 'Lowest Sales Month'
                ELSE 'Normal'
            END AS Month_Tag
        FROM monthly
        ORDER BY Total_Sales DESC
    """
    return engine.run(sql)





def seasonal_patterns():
    sql = """
        WITH monthly AS (
            SELECT
                STRFTIME('%m', STRPTIME("Order Date", '%m/%d/%Y')) AS Month_Num,
                CASE STRFTIME('%m', STRPTIME("Order Date", '%m/%d/%Y'))
                    WHEN '01' THEN 'January'
                    WHEN '02' THEN 'February'
                    WHEN '03' THEN 'March'
                    WHEN '04' THEN 'April'
                    WHEN '05' THEN 'May'
                    WHEN '06' THEN 'June'
                    WHEN '07' THEN 'July'
                    WHEN '08' THEN 'August'
                    WHEN '09' THEN 'September'
                    WHEN '10' THEN 'October'
                    WHEN '11' THEN 'November'
                    WHEN '12' THEN 'December'
                END AS Month_Name,
                ROUND(SUM(Sales), 2) AS Avg_Monthly_Sales
            FROM superstore
            GROUP BY Month_Num, Month_Name
        )
        SELECT
            Month_Num,
            Month_Name,
            Avg_Monthly_Sales,
            CASE
                WHEN Avg_Monthly_Sales > AVG(Avg_Monthly_Sales) OVER() * 1.2 THEN 'Peak Season'
                WHEN Avg_Monthly_Sales < AVG(Avg_Monthly_Sales) OVER() * 0.8 THEN 'Low Season'
                ELSE 'Normal'
            END AS Season_Tag
        FROM monthly
        ORDER BY Month_Num
    """
    return engine.run(sql)







def pareto_analysis():
    sql = """
        WITH category_sales AS (
            SELECT
                Category,
                ROUND(SUM(Sales), 2) AS Total_Sales
            FROM superstore
            GROUP BY Category
        ),
        total AS (
            SELECT SUM(Total_Sales) AS Grand_Total FROM category_sales
        ),
        ranked AS (
            SELECT
                c.Category,
                c.Total_Sales,
                ROUND(c.Total_Sales / t.Grand_Total * 100, 2) AS Revenue_Contribution_Pct,
                ROUND(SUM(c.Total_Sales) OVER(ORDER BY c.Total_Sales DESC) / t.Grand_Total * 100, 2) AS Cumulative_Pct
            FROM category_sales c, total t
        )
        SELECT
            Category,
            Total_Sales,
            Revenue_Contribution_Pct,
            Cumulative_Pct,
            CASE
                WHEN Cumulative_Pct <= 80 THEN 'Top 80% Revenue Driver'
                ELSE 'Long Tail'
            END AS Pareto_Tag
        FROM ranked
        ORDER BY Total_Sales DESC
    """
    return engine.run(sql)