import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

np.random.seed(42)
fechas = pd.date_range('2023-01-01','2024-12-31',freq='D')
n_productos = ['Laptop','Mouse','Teclado','Monitor','Auriculares']
regiones = ['Norte','Sur','Este','Oeste','Centro']

data = []
for fecha in fechas:
    for _ in range(np.random.poisson(10)):
        data.append({
            'fecha': fecha,
            'producto':np.random.choice(n_productos),
            'region':np.random.choice(regiones),
            'cantidad':np.random.randint(1, 6),
            'precio_unitario':np.random.uniform(50,1500),
            'vendedor':f'vendedor_{np.random.randint(1, 21)}'
        })

df = pd.DataFrame(data)
df['venta_total']= df['cantidad']*df['precio_unitario']

print("Shape del dataset:", df.shape)
print("\nPrimmeras filas:")
print(df.head())
print("\nInformación general:")
print(df.info())
print("\nEstadisticas descriptivas:")
print(df.describe())

df_monthly = df.groupby(df['fecha'].dt.to_period('M'))['venta_total'].sum().reset_index()
df_monthly['fecha'] = df_monthly['fecha'].astype(str)

fig_monthly = px.line(df_monthly, x='fecha', y='venta_total',
                      title='Tendencia de Ventas Mensuales',
                      labels={'venta_total':'Ventas ($)', 'fecha':'Mes'})
fig_monthly.update_traces(line=dict(width=3))

df_productos = df.groupby('producto')['venta_total'].sum().sort_values(ascending=False)
fig_productos = px.bar(x=df_productos.values, y=df_productos.index,
                       orientation='h', title='Ventas por Producto',
                       labels={'x':'Ventas Totales ($)', 'y':'Producto'})

df_regiones = df.groupby('region')['venta_total'].sum().reset_index()
fig_regiones = px.pie(df_regiones, values='venta_total',names='region',
                      title='Distribución de Ventas por Región')

df_corr = df[['cantidad','precio_unitario','venta_total']].corr()
fig_heatmap = px.imshow(df_corr,text_auto=True, aspect="auto",
                        title='Correlacion entre Variable Numericas')

fig_dist = px.histogram(df, x='venta_total', nbins=50,
                        title='Distribución de Ventas Individuales')

st.set_page_config(page_title="Dashwoard de Ventas",
                   page_icon="📊", layout="wide")

st.title("📊 Dashboard de Anáñlisis de Ventas")
st.markdown("---")

st.sidebar.header("Filtros")
productos_seleccionados = st.sidebar.multiselect(
    "Selecciona Productos:",
    options=df['producto'].unique(),
    default=df['producto'].unique()
)

regiones_seleccionados = st.sidebar.multiselect(
    "Selecciona Regiones:",
    options=df['region'].unique(),
    default=df['region'].unique()
)

df_filtered = df[
    (df['producto'].isin(productos_seleccionados)) & 
    (df['region'].isin(regiones_seleccionados))
]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Ventas Totales", f"${df_filtered['venta_total'].sum():,.0f}")
with col2:
    st.metric("Promedio pro Venta", f"${df_filtered['venta_total'].mean():,.0f}")
with col3:
    st.metric("Numero de Ventas", f"{len(df_filtered):,}")
with col4:
    crecimiento = ((df_filtered[df_filtered ['fecha'] >= '2024-01-01']['venta_total'].sum()/
                     df_filtered[df_filtered ['fecha'] < '2024-01-01']['venta_total'].sum())-1)*100
    st.metric("Crecimiento 2024", f"{crecimiento:.1f}%")

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_monthly,use_container_width=True)
    st.plotly_chart(fig_productos,use_container_width=True)
with col2:
    st.plotly_chart(fig_regiones,use_container_width=True)
    st.plotly_chart(fig_heatmap,use_container_width=True)

st.plotly_chart(fig_dist,use_container_width=True)
