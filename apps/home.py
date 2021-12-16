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
    st.write('# file excel Asli')

    df = pd.read_csv(excel_file)

    st.dataframe(df)
