# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 03:24:32 2023

@author: Tina
"""
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Data Sets',layout='wide')

st.title('Data Sets:floppy_disk:')
df=pd.read_excel('marketing_campaign1.xlsx')
df_1=pd.read_csv('df_1.csv').drop(['Unnamed: 0'],axis=1)
df_passed=pd.read_csv('passed_data.csv').drop(['Unnamed: 0'],axis=1)
tab1,tab2,tab3=st.tabs(['Original data set','DataSet after Feature Engg','DataSet passed to model for clustering'])
with st.container():
    with tab1:
        st.write("Original data set")
        st.write('Number of columns:',len(df.columns),'\nNumbers of row:',len(df))
        st.write(df)
with st.container():
    with tab2:
        st.write("DataSet after Feature Engg")
        st.write('Number of columns:',len(df_1.columns),'\nNumbers of row:',len(df_1))
        st.write(df_1)
with st.container():
    with tab3:
        st.write("DataSet passed to model for clustering")
        st.write('Number of columns:',len(df_passed.columns),'\nNumbers of row:',len(df_passed))
        st.write(df_passed)
        
        
css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.5rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)