import pandas as pd
import os

class DataWarehouse:

    @staticmethod
    def load_table(table: str) -> pd.DataFrame:
        base_project_path = "/".join(__file__.split("/")[:-1])

        table_file = f"{base_project_path}/tables/{table}.csv"
        if not os.path.exists(table_file):
            raise Exception(f"Table not exist in Data Warehouse!")
        
        return pd.read_csv(table_file)
