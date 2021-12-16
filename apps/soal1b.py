from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from logging import basicConfig
from os import rename
import numpy as np
from pandas.core import indexing
from pandas.core.indexes.base import Index
import streamlit as st
import json
import pandas as pd
import plotly.express as px
import json

def app():
    
    excel_file = 'produksi_minyak_mentah.csv' 

    df = pd.read_csv(excel_file)

    #OPEN JSON
    with open("kode_negara_lengkap.json") as f:
        data = json.load(f)

    #MENGGANTI KODE NEGARA DENGAN NAMA NEGARA LENGKAP
    konversi = {item['alpha-3'] : item['name'] for item in data}
    df.loc[:, 'kode_negara'] = df['kode_negara'].map(konversi)

    #MENGHILANGKAN DATA NaN
    df.dropna(subset=["kode_negara"], inplace=True)

    st.write("# Tahun Produksi Terbanyak")

    
    
    tahunminyak = df['tahun'].unique().tolist()
    minyaktahun = st.selectbox("Tahun",tahunminyak)
    df2 = df.loc[df['tahun'] == minyaktahun].sort_values(
    by=['produksi'], ascending=False)
    B1 = int(st.number_input("Banyak Negara", min_value=1, max_value=len(df2)))
    df2 = df2.nlargest(B1, columns='produksi')
    
    dfn = df2.rename(columns = {'kode_negara':'Negara'}, inplace = True)
    st.dataframe(dfn)

    bar_chart = px.bar(df2,x='Negara',y='produksi')
    st.plotly_chart(bar_chart)
