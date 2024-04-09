import pandas as pd
import streamlit as st
from PIL import Image

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=65918408&single=true&output=csv'
df = pd.read_csv(url)

st.title('🍫Esta es la dulcería 🍬')

listadulces = df['categoría'].unique().tolist()

selecc = st.selectbox('Selecciona la lista', listadulces)

st.dataframe(df[df['categoría'] == selecc])

urlc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=1699633182&single=true&output=csv'
dfc = pd.read_csv(urlc)

compra = {}
nombre =  st.text_input('¿Cuál es tu nombre?')
compra["nombre"] = nombre

producto = st.text_input('¿Qué vas a comprar? ')
compra["producto"] = producto
precio = df.loc[df['producto'] == producto,'precio'].values[0]

image = Image.open(str(producto)+'.png')
st.image(image)

cantidad = st.number_input('¿Cuántas piezas?',value=0)
compra["cantidad"] = cantidad


dfc.loc[0] = compra

st.dataframe(dfc[['nombre','producto','cantidad']])
pago = precio * dfc['cantidad'].values[0]

dfc['pago'] = pago



st.title('Muchas gracias por la compra 🙏🏼')
st.dataframe(dfc)
