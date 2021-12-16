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

    with open('kode_negara_lengkap.json') as f:
            data = json.load(f)
            names = dict()
            for x in data:
                country = x['name']
                idc = x['alpha-3']
                names[idc] = country

    st.write("# Tahun Produksi Terbanyak")

    frame3 = pd.read_csv(excel_file)
    frame3['kode_negara'].replace(to_replace=['AUS', 'AUT', 'BEL', 'CAN', 'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NZL', 'NOR', 'POL', 'PRT', 'SVK', 'ESP', 'SWE', 'CHE', 'TUR', 'GBR', 'USA', 'ALB', 'DZA', 'ARG', 'ARM', 'AZE', 'BGD', 'BLR', 'BIH', 'BRA', 'BRN', 'BGR', 'KHM', 'CHL', 'CHN', 'COL', 'HRV', 'CYP', 'EGY', 'EST', 'ETH', 'GEO', 'GHA', 'HTI', 'HKG', 'IND', 'IDN', 'IRN', 'ISR', 'KAZ', 'LVA', 'LTU', 'MKD', 'MYS', 'MLT', 'MDA', 'MOZ', 'NGA', 'PAK', 'PRY', 'PER', 'PHL', 'ROU', 'RUS', 'SAU', 'SGP', 'SVN', 'ZAF', 'SDN', 'TWN', 'TZA', 'THA', 'UKR', 'ARE', 'URY', 'VNM', 'ZMB', 'SRB', 'MNE', 'AGO', 'BHR', 'BEN', 'BOL', 'BWA', 'CMR', 'COG', 'CRI', 'CIV', 'CUB', 'PRK', 'COD', 'DOM', 'ECU', 'SLV', 'ERI', 'GAB', 'GTM', 'HND', 'IRQ', 'JAM', 'JOR', 'KEN', 'KWT', 'KGZ', 'LBN', 'LBY', 'MNG', 'MAR', 'MMR', 'NAM', 'NPL', 'NIC', 'NER', 'OMN', 'PAN', 'QAT', 'SEN', 'LKA', 'SYR', 'TJK', 'TGO', 'TTO', 'TUN', 'TKM', 'UZB', 'VEN', 'YEM', 'ZWE'],value=[names['AUS'], names['AUT'], names['BEL'], names['CAN'], names['CZE'], names['DNK'], names['FIN'], names['FRA'], names['DEU'], names['GRC'], names['HUN'], names['ISL'], names['IRL'], names['ITA'], names['JPN'], names['KOR'], names['LUX'], names['MEX'], names['NLD'], names['NZL'], names['NOR'], names['POL'], names['PRT'], names['SVK'], names['ESP'], names['SWE'], names['CHE'], names['TUR'], names['GBR'], names['USA'], names['ALB'], names['DZA'], names['ARG'], names['ARM'], names['AZE'], names['BGD'], names['BLR'], names['BIH'], names['BRA'], names['BRN'], names['BGR'], names['KHM'], names['CHL'], names['CHN'], names['COL'], names['HRV'], names['CYP'], names['EGY'], names['EST'], names['ETH'], names['GEO'], names['GHA'], names['HTI'], names['HKG'], names['IND'], names['IDN'], names['IRN'], names['ISR'], names['KAZ'], names['LVA'], names['LTU'], names['MKD'], names['MYS'], names['MLT'], names['MDA'], names['MOZ'], names['NGA'], names['PAK'], names['PRY'], names['PER'], names['PHL'], names['ROU'], names['RUS'], names['SAU'], names['SGP'], names['SVN'], names['ZAF'], names['SDN'], names['TWN'], names['TZA'], names['THA'], names['UKR'], names['ARE'], names['URY'], names['VNM'], names['ZMB'], names['SRB'], names['MNE'], names['AGO'], names['BHR'], names['BEN'], names['BOL'], names['BWA'], names['CMR'], names['COG'], names['CRI'], names['CIV'], names['CUB'], names['PRK'], names['COD'], names['DOM'], names['ECU'], names['SLV'], names['ERI'], names['GAB'], names['GTM'], names['HND'], names['IRQ'], names['JAM'], names['JOR'], names['KEN'], names['KWT'], names['KGZ'], names['LBN'], names['LBY'], names['MNG'], names['MAR'], names['MMR'], names['NAM'], names['NPL'], names['NIC'], names['NER'], names['OMN'], names['PAN'], names['QAT'], names['SEN'], names['LKA'], names['SYR'], names['TJK'], names['TGO'], names['TTO'], names['TUN'], names['TKM'], names['UZB'], names['VEN'], names['YEM'], names['ZWE']],inplace=True)

    negaraminyak2 = frame3['kode_negara'].unique().tolist()
    tahunminyak = frame3['tahun'].unique().tolist()
    minyaktahun = st.multiselect("Tahun",tahunminyak, default=tahunminyak)
    minyak_selection2 = st.multiselect("Negara:",negaraminyak2, default=negaraminyak2)
    filter2 =  (frame3['kode_negara'].isin(minyak_selection2) & frame3['tahun'].isin(minyaktahun))
    frame3 = frame3[filter2].groupby(by=['tahun']).sum()[["produksi"]].sort_values(by='produksi')
    bar_sum = px.bar(frame3,x='produksi',y=frame3.index)
    st.plotly_chart(bar_sum)
