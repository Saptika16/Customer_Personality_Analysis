# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 02:13:07 2023

@author: Tina
"""
#libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle

st.set_page_config(page_title='Clustering',layout='wide')
st.set_option('deprecation.showPyplotGlobalUse',False)
st.title("Clusteing")



filename='trained_kmeans.sav'
loaded_model=pickle.load(open(filename, 'rb'))
df=pd.read_excel('marketing_campaign1.xlsx')
df_passed=pd.read_csv('passed_data.csv').drop(['Unnamed: 0'],axis=1)
df_1=pd.read_csv('df_1.csv').drop(['Unnamed: 0'],axis=1)
df_with_cluster=pd.read_csv('df_with_cluster.csv').drop(['Unnamed: 0'],axis=1)
column1, column2 = st.columns([1,2])
with column1:
    curve=st.selectbox('Select to plot to view:',['Cluster Scatter','clusters count','Data based on Clusters',
                                                  'Scree','elbow',
                         'Expenditure~Income','Expenditure~Meat',
                         'Purchase Methods based on Clusters',
                        'Age based on clusters', 'Website Visit last month based on cluster',
                       'family dynamics based on cluster', 'Discount per cluster'
                       ])
    
with column2:
    #
    if curve=='Scree':
        #with column1:
           st.image('scree.png')
    elif curve=='elbow':
        #with column1:
            st.image('elbow.png')
    elif curve=='Cluster Scatter':
        st.image('cluster_scatter.png')
        
    elif curve=='clusters count':
        #with column1:
            st.image('5cluster.png')
            with column1:
               st.write('Lowest economic status people has highest in number')
    elif curve=='Expenditure~Income':
        #with column1:
             st.image('expenditure_Income.png')       
    elif curve=='Expenditure~Meat':
        #with column1:
             st.image('expenditure_onMeat.png')       
    elif curve=='Purchase Methods based on Clusters':
        #with column1:
             st.image('cluster_exp_product.png')       
    elif curve=='Age based on clusters':
        #with column1:
             st.image('cluster_agedivide.png')       
    elif curve=='Website Visit last month based on cluster':
        #with column1:
             st.image('cluster_avgwebvisit.png')       
    elif curve=='family dynamics based on cluster':
       # with column1:
             st.image('cluster_familydynamics.png')       
    elif curve=='Discount per cluster':
       # with column1:
             st.image('dicount_per_cluster.png')       
    elif curve=='Data based on Clusters':
        #with column1:
            for c in df_with_cluster.drop(['Cluster'],axis=1):
                grid=sns.FacetGrid(df_with_cluster,col='Cluster')
                grid=grid.map(plt.hist,c)
                plt.show()
                st.pyplot(figsize=(5,5))
            #st.image('cluster_facet.png')       
                   
