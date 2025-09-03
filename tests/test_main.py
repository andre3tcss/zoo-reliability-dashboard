import unittest
import pandas as pd
from zoo.main import load_data

def test_load_datas_return_dataFrame(self):
    df = ('dados_performance.csv')
    self.assertIsInstance(df, pd.DataFrame)
    colunas_esperadas = {"timestamp", "cpu_usage_percent", "memory_usage_mb", "api_response_time_ms"}
    self.assertTrue(colunas_esperadas.issubset(df.columns))