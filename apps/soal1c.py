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
    
    

    st.write("# Negara Produksi Terbanyak")
    
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
    negaraminyak.sort()
    minyak_selection = st.multiselect("Negara:",negaraminyak, default=negaraminyak)
    fil3 =  (df['kode_negara'].isin(minyak_selection))
    df = df[fil3].groupby(by=['kode_negara']).sum()[["produksi"]].sort_values(by='produksi')

    df2 = df.nlargest(1, columns='produksi')
    st.write('*** Negara Dengan Produksi Terbanyak Secara Komulatif :***',df2.index.unique())
    st.write('*** Dengan Jumlah Produksi :***',df2['produksi'].unique())
    
    bar_country = px.bar(
        df,x=df.index,y='produksi'
        )
    st.plotly_chart(bar_country)
