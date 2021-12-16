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

    df2 = pd.read_csv(excel_file)
    df2['kode_negara'].replace(to_replace=['AUS', 'AUT', 'BEL', 'CAN', 'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'SVK', 'ESP', 'SWE', 'CHE', 'TUR', 'GBR', 'USA', 'ALB', 'DZA', 'ARG', 'ARM', 'AZE', 'BGD', 'BLR', 'BIH', 'BRA', 'BRN', 'BGR', 'KHM', 'CHL', 'CHN', 'COL', 'HRV', 'CYP', 'EGY', 'EST', 'ETH', 'GEO', 'GHA', 'HTI', 'HKG', 'IND', 'IDN', 'IRN', 'ISR', 'KAZ', 'LVA', 'LTU', 'MKD', 'MYS', 'MLT', 'MDA', 'MOZ', 'NGA', 'PAK', 'PRY', 'PER', 'PHL', 'ROU', 'RUS', 'SAU', 'SGP', 'SVN', 'ZAF', 'SDN', 'TWN', 'TZA', 'THA', 'UKR', 'ARE', 'URY', 'VNM', 'ZMB', 'SRB', 'MNE', 'AGO', 'BHR', 'BEN', 'BOL', 'BWA', 'CMR', 'COG', 'CRI', 'CIV', 'CUB', 'PRK', 'COD', 'DOM', 'ECU', 'SLV', 'ERI', 'GAB', 'GTM', 'HND', 'IRQ', 'JAM', 'JOR', 'KEN', 'KWT', 'KGZ', 'LBN', 'LBY', 'MNG', 'MAR', 'MMR', 'NAM', 'NPL', 'NIC', 'NER', 'OMN', 'PAN', 'QAT', 'SEN', 'LKA', 'SYR', 'TJK', 'TGO', 'TTO', 'TUN', 'TKM', 'UZB', 'VEN', 'YEM', 'ZWE'],value=[names['AUS'], names['AUT'], names['BEL'], names['CAN'], names['CZE'], names['DNK'], names['FIN'], names['FRA'], names['DEU'], names['GRC'], names['HUN'], names['ISL'], names['IRL'], names['ITA'], names['JPN'], names['KOR'], names['LUX'], names['MEX'], names['NLD'], names['NZL'], names['NOR'], names['POL'], names['PRT'], names['SVK'], names['ESP'], names['SWE'], names['CHE'], names['TUR'], names['GBR'], names['USA'], names['ALB'], names['DZA'], names['ARG'], names['ARM'], names['AZE'], names['BGD'], names['BLR'], names['BIH'], names['BRA'], names['BRN'], names['BGR'], names['KHM'], names['CHL'], names['CHN'], names['COL'], names['HRV'], names['CYP'], names['EGY'], names['EST'], names['ETH'], names['GEO'], names['GHA'], names['HTI'], names['HKG'], names['IND'], names['IDN'], names['IRN'], names['ISR'], names['KAZ'], names['LVA'], names['LTU'], names['MKD'], names['MYS'], names['MLT'], names['MDA'], names['MOZ'], names['NGA'], names['PAK'], names['PRY'], names['PER'], names['PHL'], names['ROU'], names['RUS'], names['SAU'], names['SGP'], names['SVN'], names['ZAF'], names['SDN'], names['TWN'], names['TZA'], names['THA'], names['UKR'], names['ARE'], names['URY'], names['VNM'], names['ZMB'], names['SRB'], names['MNE'], names['AGO'], names['BHR'], names['BEN'], names['BOL'], names['BWA'], names['CMR'], names['COG'], names['CRI'], names['CIV'], names['CUB'], names['PRK'], names['COD'], names['DOM'], names['ECU'], names['SLV'], names['ERI'], names['GAB'], names['GTM'], names['HND'], names['IRQ'], names['JAM'], names['JOR'], names['KEN'], names['KWT'], names['KGZ'], names['LBN'], names['LBY'], names['MNG'], names['MAR'], names['MMR'], names['NAM'], names['NPL'], names['NIC'], names['NER'], names['OMN'], names['PAN'], names['QAT'], names['SEN'], names['LKA'], names['SYR'], names['TJK'], names['TGO'], names['TTO'], names['TUN'], names['TKM'], names['UZB'], names['VEN'], names['YEM'], names['ZWE']],inplace=True)

    negaraminyak = df2['kode_negara'].unique()
    minyak_selection = st.selectbox('Pilih :', negaraminyak)

    if minyak_selection in ('WLD','G20','OECD','EU28','OEU'):
        st.write("Negara yang dipilih : ")
        st.write("Kode Negara : ")
        st.write("Region :")
        st.write("Sub Region :")
    else:
        selectkode = namakey[minyak_selection]
        st.write("Negara yang dipilih : ",names[selectkode])
        st.write("Kode Negara : ",alpha3[selectkode])
        st.write("Region :",region[selectkode])
        st.write("Sub Region :",subregion[selectkode])

    filterbanyak = df2[df2.kode_negara== minyak_selection]
    filterbanyak = filterbanyak.nlargest(1, columns='produksi')

    filtersedikit = df2[df2.kode_negara== minyak_selection]
    filtersedikit = filtersedikit.nsmallest(44, columns='produksi')
    newfilter = filtersedikit.loc[filtersedikit[filtersedikit.produksi > 0].groupby(by='kode_negara')['produksi'].idxmin()]
    newfilter = newfilter.nsmallest(1, columns='produksi')


    seluruhtahun = df2[df2.kode_negara== minyak_selection]

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
