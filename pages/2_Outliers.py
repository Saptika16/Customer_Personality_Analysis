# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:13:15 2023

@author: Tina
"""
import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(page_title='Clustering',layout='wide')
st.title('Outliers :round_pushpin:')
df=pd.read_excel('marketing_campaign1.xlsx')
st.set_option('deprecation.showPyplotGlobalUse',False)


column1, column2 ,column3= st.columns([1,1,1])


with column1:
    st.subheader('Income')
    sns.boxplot(df['Income'])
    st.pyplot()
with column2:
    st.subheader('Expenditure on Meat')
    sns.boxplot(df['MntMeatProducts'])
    st.pyplot()
with column3:
    st.subheader('Age')
    st.image('age_boxplot.png')
