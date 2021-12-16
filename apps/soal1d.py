from contextlib import nullcontext
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

    st.write('# Soal 1 D')

    with open('kode_negara_lengkap.json') as f:
            data = json.load(f)
            names = dict()
            region = dict()
            alpha3 = dict()
            subregion = dict()
            namakey = dict()
            for x in data:
                country = x['name']
                idc = x['alpha-3']
                names[idc] = country
                alpha3[idc] = x['country-code']
                region[idc] = x['region']
                subregion[idc] = x['sub-region']
                namakey[country] = idc


    df = pd.read_csv(excel_file)

    #OPEN JSON
    with open("kode_negara_lengkap.json") as f:
        data = json.load(f)

    #MENGGANTI KODE NEGARA DENGAN NAMA NEGARA LENGKAP
    konversi = {item['alpha-3'] : item['name'] for item in data}
    df.loc[:, 'kode_negara'] = df['kode_negara'].map(konversi)

    #MENGHILANGKAN DATA NaN
    df.dropna(subset=["kode_negara"], inplace=True)

    negaraminyak = df['kode_negara'].unique()
    negaraminyak.sort()
    minyak_selection = st.selectbox('Pilih :', negaraminyak)

    selectkode = namakey[minyak_selection]
    st.write("Negara yang dipilih : ",names[selectkode])
    st.write("Kode Negara : ",alpha3[selectkode])
    st.write("Region :",region[selectkode])
    st.write("Sub Region :",subregion[selectkode])

    filterbanyak = df[df.kode_negara== minyak_selection]
    filterbanyak = filterbanyak.nlargest(1, columns='produksi')

    filtersedikit = df[df.kode_negara== minyak_selection]
    filtersedikit = filtersedikit.nsmallest(44, columns='produksi')
    newfilter = filtersedikit.loc[filtersedikit[filtersedikit.produksi > 0].groupby(by='kode_negara')['produksi'].idxmin()]
    newfilter = newfilter.nsmallest(1, columns='produksi')


    seluruhtahun = df[df.kode_negara== minyak_selection]

    st.markdown("<h3 style='text-align: left; color: grey;'>Tahun Terbanyak</h3>", unsafe_allow_html=True)
    if filterbanyak['produksi'].unique() == 0:
        st.write('Tidak ada produksi')
    else:
        st.dataframe(filterbanyak)
    st.markdown("<h3 style='text-align: left; color: grey;'>Tahun Tersedikit</h3>", unsafe_allow_html=True)
    if newfilter.empty:
        st.write('Tidak ada produksi')
    else:
        st.dataframe(newfilter)
    st.markdown("<h3 style='text-align: left; color: grey;'>Produksi Seluruh Tahun</h3>", unsafe_allow_html=True)
    st.dataframe(seluruhtahun)
