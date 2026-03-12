from utils.db import QueryEngine

engine = QueryEngine("data/superstore.csv")

def best_selling_products():
    sql = """
        SELECT
            "Product Name",
            Category,
            "Sub-Category",
            ROUND(SUM(Sales), 2) AS Total_Revenue,
            SUM(Quantity) AS Total_Quantity_Sold,
            RANK() OVER(ORDER BY SUM(Sales) DESC) AS Revenue_Rank
        FROM superstore
        GROUP BY "Product Name", Category, "Sub-Category"
        ORDER BY Total_Revenue DESC
        LIMIT 20
    """
    return engine.run(sql)


def most_profitable_products():
    sql = """
        SELECT
            "Product Name",
            Category,
            "Sub-Category",
            ROUND(SUM(Sales), 2) AS Total_Revenue,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            CASE 
                WHEN SUM(Sales) = 0 THEN NULL
                ELSE ROUND(SUM(Profit) / SUM(Sales) * 100, 2)
            END AS Profit_Margin_Pct,
            RANK() OVER(ORDER BY SUM(Profit) DESC) AS Profit_Rank
        FROM superstore
        GROUP BY "Product Name", Category, "Sub-Category"
        ORDER BY Total_Profit DESC
        LIMIT 20
    """
    return engine.run(sql)



def negative_margin_products():
    sql = """
        SELECT
            "Product Name",
            Category,
            "Sub-Category",
            ROUND(SUM(Sales), 2) AS Total_Revenue,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct
        FROM superstore
        GROUP BY "Product Name", Category, "Sub-Category"
        HAVING SUM(Profit) < 0
        ORDER BY Total_Profit ASC
    """
    return engine.run(sql)


def product_profit_margin_analysis():
    sql = """
        SELECT
            "Product Name",
            Category,
            "Sub-Category",
            ROUND(SUM(Sales), 2) AS Total_Revenue,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin_Pct,
            CASE
                WHEN SUM(Profit) / SUM(Sales) * 100 >= 30 THEN 'Premium Product'
                WHEN SUM(Profit) / SUM(Sales) * 100 BETWEEN 10 AND 30 THEN 'Healthy Margin'
                WHEN SUM(Profit) / SUM(Sales) * 100 BETWEEN 0 AND 10 THEN 'Low Margin'
                ELSE 'Loss Making'
            END AS Margin_Category
        FROM superstore
        GROUP BY "Product Name", Category, "Sub-Category"
        ORDER BY Profit_Margin_Pct DESC
    """
    return engine.run(sql)




def product_pareto_analysis():
    sql = """
        WITH product_sales AS (
            SELECT
                "Product Name",
                Category,
                ROUND(SUM(Sales), 2) AS Total_Revenue
            FROM superstore
            GROUP BY "Product Name", Category
        ),
        total AS (
            SELECT SUM(Total_Revenue) AS Grand_Total FROM product_sales
        ),
        ranked AS (
            SELECT
                p."Product Name",
                p.Category,
                p.Total_Revenue,
                ROUND(p.Total_Revenue / t.Grand_Total * 100, 2) AS Revenue_Contribution_Pct,
                ROUND(SUM(p.Total_Revenue) OVER(ORDER BY p.Total_Revenue DESC) / t.Grand_Total * 100, 2) AS Cumulative_Pct
            FROM product_sales p, total t
        )
        SELECT
            "Product Name",
            Category,
            Total_Revenue,
            Revenue_Contribution_Pct,
            Cumulative_Pct,
            CASE
                WHEN Cumulative_Pct <= 80 THEN 'Top 80% Revenue Driver'
                ELSE 'Long Tail'
            END AS Pareto_Tag
        FROM ranked
        ORDER BY Total_Revenue DESC
    """
    return engine.run(sql)