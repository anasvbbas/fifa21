import pandas as pd
import streamlit as st

fifa = pd.read_csv('fifa21clean.csv')

st.title('Fifa 21 Player Lists')
st.dataframe(fifa)
