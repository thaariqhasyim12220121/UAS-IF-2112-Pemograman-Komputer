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

    negaraminyak = df['kode_negara'].unique().tolist()
    
    
    minyak_selection = st.selectbox('Negara:', negaraminyak)

    st.write("Negara yang dipilih : ",minyak_selection)

    filter = df[df.kode_negara== minyak_selection]


    bar_chart = px.bar(filter,x='tahun',y='produksi')
    st.plotly_chart(bar_chart)
