# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:13:15 2023

@author: Tina
"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title='Clustering',layout='wide')
df=pd.read_excel('marketing_campaign1.xlsx')
st.set_option('deprecation.showPyplotGlobalUse',False)
st.markdown('<style>body(bakground-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Outliers")


tab1,tab2,tab3=st.tabs(['Income','Expenditure on Meat','Age'])
tab1.subheader('Income')
with st.container():
    sns.boxplot(df['Income'])
    tab1.pyplot(figsize=(5,5))
tab2.subheader('Expenditure on Meat')
with st.container():
    sns.boxplot(df['MntMeatProducts'])
    tab2.pyplot(figsize=(5,5))

tab3.subheader('Age')
with st.container():
    tab3.image('age_boxplot.png')
