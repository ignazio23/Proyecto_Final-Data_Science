
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
#import pyarrow.parquet as pq 
#from streamlit import radio, sidebar, markdown, title, image, checkbox, selectbox, container, columns, multiselect, button, table, image


@st.cache_data
def get_restaurant(fn/gr):
    return pd.read_parquet(file1)
file1 = "https://storage.googleapis.com/yelp-and-maps-data-processed/df_resto_user_final.parquet"
df_restaurant = get_restaurant(file1)

df_FL = df_restaurant[df_restaurant['ubicacion'] == 'Florida']
df_PA = df_restaurant[df_restaurant['ubicacion'] == 'Pennsylvania']
df_CA = df_restaurant[df_restaurant['ubicacion'] == 'California']
df_IL = df_restaurant[df_restaurant['ubicacion'] == 'Illinois']

df_user = df_restaurant['user_id'].unique()
df_user_head = df_user[:20]

def get_user(fn2/gu):
    return pd.read_parquet(file2)
file2 = "https://storage.googleapis.com/yelp-and-maps-data-processed/highRest_dummies.parquet"
highdf = get_user(file2)

# Sidebar con Opciones
st.sidebar.image("https://github.com/ignazio23/Proyecto_Final-Data_Science/blob/main/Utility/2024-02-15%2020_24_21-Window.png?raw=true", width=300)
sidebar_option = st.sidebar.radio("Elige una Opción", ["Inicio", "Crush", "Popular Destination","Dashboard"])


# Fondo del Sidebar
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #D5BA98;
    }
</style>
""", unsafe_allow_html=True)
