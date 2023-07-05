# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 03:24:32 2023

@author: Tina
"""
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Data Sets',layout='wide')
df=pd.read_excel('marketing_campaign1.xlsx')
df_1=pd.read_csv('df_1.csv').drop(['Unnamed: 0'],axis=1)
df_passed=pd.read_csv('passed_data.csv').drop(['Unnamed: 0'],axis=1)
with st.container():
    st.write("Original data set")
    st.write('Number of columns:',len(df.columns),'\nNumbers of row:',len(df))
    st.write(df)
with st.container():
    st.write("Cleaned data set")
    st.write('Number of columns:',len(df_1.columns),'\nNumbers of row:',len(df_1))
    st.write(df_1)
with st.container():
    st.write("Passed data set")
    st.write('Number of columns:',len(df_passed.columns),'\nNumbers of row:',len(df_passed))
    st.write(df_passed)