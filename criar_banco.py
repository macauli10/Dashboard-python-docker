import sqlite3
import pandas as pd

df = pd.read_csv("data/processed/dados_tratados.csv")
conn = sqlite3.connect("db/superstore.db")
df.to_sql("vendas", conn, if_exists="replace", index=False)
conn.close()
