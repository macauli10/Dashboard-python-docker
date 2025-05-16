# dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3


conn = sqlite3.connect("db/superstore.db")

# Lê os dados
df = pd.read_sql_query("SELECT * FROM vendas", conn)
conn.close()

# Seu código de Streamlit continua aqui...

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
sns.set_style("whitegrid")

# Título e descrição
st.markdown("# 📊 Dashboard de Vendas - Superstore")
st.markdown("Análise interativa de vendas, lucro e categorias de produtos.")
st.markdown("---")

# Carregamento de dados
df = pd.read_csv('data/processed/dados_tratados.csv')

# Filtros
st.sidebar.header("Filtros")
segmento = st.sidebar.multiselect("Segmento", df["segmento"].unique(), default=df["segmento"].unique())
regiao = st.sidebar.multiselect("Região", df["regiao"].unique(), default=df["regiao"].unique())

df_filtrado = df[(df["segmento"].isin(segmento)) & (df["regiao"].isin(regiao))]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas", f"R$ {df_filtrado['total_vendido'].sum():,.2f}")
col2.metric("Lucro Total", f"R$ {df_filtrado['lucro'].sum():,.2f}")
col3.metric("Total de Pedidos", df_filtrado['id_pedido'].nunique())

st.markdown("---")

# Visualizações
col1, col2 = st.columns(2)

with col1:
    st.subheader("Total Vendido por Categoria")
    vendas_categoria = df_filtrado.groupby("categoria")["total_vendido"].sum().sort_values()
    st.bar_chart(vendas_categoria)

with col2:
    st.subheader("Lucro por Sub-Categoria")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df_filtrado, x="lucro", y="sub_categoria", palette="crest", ax=ax)
    ax.set_title("Lucro por Sub-Categoria")
    st.pyplot(fig)
