import streamlit as st
import time
import numpy as np
import pandas as pd
import altair as alt

def app():
    

    #import & linking json with csv
    jsondata = pd.read_json("kode_negara_lengkap.json")
    df = pd.read_csv("produksi_minyak_mentah.csv")
    df_merge = pd.merge(df,jsondata,left_on='kode_negara',right_on='alpha-3')
    
    #sorting
    list_negara = df_merge["name"].unique().tolist()
    list_negara.sort()

    #command control streamlit
    tahunminyak = df['tahun'].unique().tolist()
    tahun = st.selectbox("Pilih tahun", tahunminyak)

    produksi = df_merge.groupby(['name', 'kode_negara', 'region', 'sub-region'])['produksi'].sum().reset_index().sort_values(by=['produksi'], ascending=False).reset_index(drop=True)
    produksimax = produksi[(produksi["produksi"] > 0)].iloc[0]
    produksimin = produksi[(produksi["produksi"] > 0)].iloc[-1]
    produksi0 = produksi[(produksi["produksi"] == 0)].sort_values(by=['name']).reset_index(drop=True)
    produksi0.index += 1

    tahunproduksi = df_merge[(df_merge["tahun"] == tahun)][['name', 'kode_negara', 'region', 'sub-region', 'produksi']].sort_values(by=['produksi'], ascending=False).reset_index(drop=True)
    tahunproduksimax = tahunproduksi[(tahunproduksi["produksi"] > 0)].iloc[0]
    tahunproduksimin = tahunproduksi[(tahunproduksi["produksi"] > 0)].iloc[-1]
    tahunproduksi0 = tahunproduksi[(tahunproduksi["produksi"] == 0)].sort_values(by=['name']).reset_index(drop=True)
    tahunproduksi0.index += 1

    
    st.markdown(
        f"""
        ### Negara Komulatif Produksi Tertinggi
        Negara: {produksimax["name"]}\n
        Kode negara: {produksimax["kode_negara"]}\n
        Region: {produksimax["region"]}\n
        Sub-region: {produksimax["sub-region"]}\n
        Jumlah produksi: {produksimax["produksi"]}\n
        ### Negara dengan jumlah produksi terbesar pada tahun {tahun}  
        Negara: {tahunproduksimax["name"]}\n
        Kode negara: {tahunproduksimax["kode_negara"]}\n
        Region: {tahunproduksimax["region"]}\n
        Sub-region: {tahunproduksimax["sub-region"]}\n
        Jumlah produksi: {tahunproduksimax["produksi"]}\n
        ### Negara dengan total produksi keseluruhan tahun terkecil tidak = 0
        Negara: {produksimin["name"]}\n
        Kode negara: {produksimin["kode_negara"]}\n
        Region: {produksimin["region"]}\n
        Sub-region: {produksimin["sub-region"]}\n
        Jumlah produksi: {produksimin["produksi"]}\n
        #### Negara dengan jumlah produksi terkecil pada tahun {tahun}  
        Negara: {tahunproduksimin["name"]}\n
        Kode negara: {tahunproduksimin["kode_negara"]}\n
        Region: {tahunproduksimin["region"]}\n
        Sub-region: {tahunproduksimin["sub-region"]}\n
        Jumlah produksi: {tahunproduksimin["produksi"]}\n
    """
    )
    st.markdown(
        """
        #### Negara dengan total produksi keseluruhan tahun sama dengan nol
        
    """
    )
    produksi0 = produksi0.drop(['produksi'], axis=1).rename(columns={"name":"Negara", "kode_negara":"Kode Negara", "region":"Region", "sub-region":"Sub Region"})
    st.dataframe(produksi0)
    st.markdown(
        f"""
        #### Negara dengan jumlah produksi sama dengan nol pada tahun {tahun}
        
    """
    )
    tahunproduksi0 = tahunproduksi0.drop(['produksi'], axis=1).rename(columns={"name":"Negara", "kode_negara":"Kode Negara", "region":"Region", "sub-region":"Sub Region"})
    st.dataframe(tahunproduksi0)
    
    st.markdown(
        """
        #### Terimakasih, Salam Thaariq Hasyim @ 2021
        
    """
    )
    
