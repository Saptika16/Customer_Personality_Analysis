# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 01:06:48 2023

@author: Tina
"""

from sklearn.preprocessing import StandardScaler 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import streamlit as st
import pickle

st.set_page_config(page_title='Clustering',layout='wide')
filename='trained_model.sav'
loaded_model=pickle.load(open(filename, 'rb'))
loaded_pca=pickle.load(open('pca.pkl','rb'))
df=pd.read_csv('df.csv')
df_1=pd.read_csv('df_1.csv')
st.set_option('deprecation.showPyplotGlobalUse',False)
st.markdown('<style>body(bakground-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Prediction")
col1,col2,col3=st.columns([1,1,1])

with st.form("my_form"):
     with col1:
            age=st.number_input('age:')
            Years_Enrolled=st.number_input('Number of year enrolled')
            Qualification=st.number_input('Qualification : (0-undergraduate or 1-graduate or 2-post graduate)')
            family=st.number_input('family ? ( 0-no or 1-yes)')
            Income=st.number_input('Income:')
            Recency=st.number_input('Recency: ( 0-less than 49 days or 1-more than 49 days)')
            Complain=st.number_input('Complained ?( 0-no or 1-yes)')
            MntWines=st.number_input('Expenditure on Wine:')
     with col2:
           
            MntFruits=st.number_input('Expenditure on Fruits:')
            MntMeatProducts=st.number_input('Expenditure on Meat Products:')
            MntFishProducts=st.number_input('Expenditure on Fish Products:')
            MntSweetProducts=st.number_input('Expenditure on Sweet Products:')
            MntGoldProds=st.number_input('Expenditure on Gold Prods:')
            NumWebVisitsMonth=st.number_input('Number of Web Visits last Month')
            NumDealsPurchases=st.number_input('Number Discount Purchases:')
            NumWebPurchases=st.number_input('Number of Web-Purchases:')
     with col3:   
            
            NumCatalogPurchases=st.number_input('Number of Catalog-Purchases:')
            NumStorePurchases=st.number_input('Number of Store-Purchases')
            AcceptedCmp1=st.number_input('Accepted Cmp 1 ? ( 0-no or 1-yes)')
            AcceptedCmp2=st.number_input('Accepted Cmp 2 ? ( 0-no or 1-yes)')
            AcceptedCmp3=st.number_input('Accepted Cmp 3 ? ( 0-no or 1-yes)')
            AcceptedCmp4=st.number_input('Accepted Cmp 4 ? ( 0-no or 1-yes)')
            AcceptedCmp5=st.number_input('Accepted Cmp 5 ? ( 0-no or 1-yes)')
            Response=st.number_input('Response ?( 0-no or 1-yes)')
            
        
        
        
     data=[[age,Years_Enrolled,Qualification, family, Income,Recency, MntWines, MntFruits, MntMeatProducts,
                      MntFishProducts, MntSweetProducts, MntGoldProds,
                      NumDealsPurchases, NumWebPurchases, NumCatalogPurchases,
                      NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3,
                      AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2,
                      Complain, Response
               ]]
     submitted=st.form_submit_button("Submit")
if submitted:
    scaler = StandardScaler()
    n_sc=scaler.fit_transform(data)
    n=loaded_pca.transform(n_sc)
    #clust=loaded_model.predict(n)[0]
    #print('Data Belongs to cluster',clust)
    
    #n=scaler.fit_transform(input_data_as_numpy_array.reshape(-1, 1))
    predicted=loaded_model.predict(n)
    #ahnged knn to loaded_model
    if (predicted[0]==0):
        a=' 1st Cluster '
        b='Lowest economic Class'
    elif (predicted[0]==1):
        a=' 2nd Cluster'
        b='Highest economic Class'
    elif (predicted[0]==2):
       a=' 3rd Cluster '
       b='Lower Middle Class'
    elif (predicted[0]==3):
       a=' 4th Cluster'
       b='Upper Middle Class'
    elif (predicted[0]==4):
       a=' 5th Cluster'
       b='Low economical Class'
    
    st.write('New data falls in ',a,'i.e.,',b)
    st.divider()
    cluster_df=df[df['Cluster']==predicted[0]]
    st.write('Other data from ',a)
    st.write(cluster_df.drop(['Cluster'],axis=1))
    #fig,ax=plt.subplots(nrows=6,ncols=3)
    for c in cluster_df.drop(['Cluster'],axis=1):
            fig,ax=plt.subplots()
            rcParams['figure.figsize'] = 11.7,8.27
            grid=sns.FacetGrid(cluster_df,col='Cluster')
            grid=grid.map(plt.hist,c)
            plt.show()
            st.pyplot(figsize=(5,2))                  
    
  
    
  