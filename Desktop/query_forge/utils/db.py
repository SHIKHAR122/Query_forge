import duckdb
import pandas as pd

class QueryEngine:
    def __init__(self, csv_path: str):
        self.conn = duckdb.connect()
        self.df = pd.read_csv(csv_path, encoding="latin1")
        self.conn.register("superstore", self.df)

    def run(self, sql: str) -> pd.DataFrame:
        return self.conn.execute(sql).fetchdf()

    def columns(self) -> list:
        return self.df.columns.tolist()