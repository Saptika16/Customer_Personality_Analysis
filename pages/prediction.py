# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 01:06:48 2023

@author: Tina
"""

from sklearn.preprocessing import StandardScaler 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle

st.set_page_config(page_title='Clustering',layout='wide')
filename='trained_model.sav'
loaded_model=pickle.load(open(filename, 'rb'))
loaded_pca=pickle.load(open('pca.pkl','rb'))
df=pd.read_csv('df.csv')
st.set_option('deprecation.showPyplotGlobalUse',False)
st.markdown('<style>body(bakground-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Prediction")

with st.form("my_form"):
    age=st.number_input('age:')
    Years_Enrolled=st.number_input('Number of year enrolled')
    Qualification=st.number_input('Qualification : (0-undergraduate or 1-graduate or 2-post graduate)')
    family=st.number_input('family ? ( 0-no or 1-yes)')
    Income=st.number_input('Income:')
    Recency=st.number_input('Recency: ( 0-less than 49 days or 1-more than 49 days)')
    MntWines=st.number_input('Wine:')
    MntFruits=st.number_input('Fruits:')
    MntMeatProducts=st.number_input('Meat Products:')
    MntFishProducts=st.number_input('Fish Products:')
    MntSweetProducts=st.number_input('Sweet Products:')
    MntGoldProds=st.number_input('Gold Prods:')
    NumDealsPurchases=st.number_input('Number Discount Purchases:')
    NumWebPurchases=st.number_input('Number of Web-Purchases:')
    NumCatalogPurchases=st.number_input('Number of Catalog-Purchases:')
    NumStorePurchases=st.number_input('Number of Store-Purchases')
    NumWebVisitsMonth=st.number_input('Number of Web Visits last Month')
    AcceptedCmp1=st.number_input('Accepted Cmp 1 ? ( 0-no or 1-yes)')
    AcceptedCmp2=st.number_input('Accepted Cmp 2 ? ( 0-no or 1-yes)')
    AcceptedCmp3=st.number_input('Accepted Cmp 3 ? ( 0-no or 1-yes)')
    AcceptedCmp4=st.number_input('Accepted Cmp 4 ? ( 0-no or 1-yes)')
    AcceptedCmp5=st.number_input('Accepted Cmp 5 ? ( 0-no or 1-yes)')
    Complain=st.number_input('Complained ?( 0-no or 1-yes)')
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
    n=scaler.fit_transform(data)
    n=loaded_pca.transform(n)
    #clust=loaded_model.predict(n)[0]
    #print('Data Belongs to cluster',clust)
    
    #n=scaler.fit_transform(input_data_as_numpy_array.reshape(-1, 1))
    predicted=loaded_model.predict(n)
    #ahnged knn to loaded_model
    if (predicted[0]==0):
        a=' 1st Cluster '
    elif (predicted[0]==1):
        a=' 2nd Cluster'
    elif (predicted[0]==2):
       a=' 3rd Cluster '
    elif (predicted[0]==3):
       a=' 4th Cluster'
    elif (predicted[0]==4):
       a=' 5th Cluster'
    st.write(a)
    cluster_df=df[df['Cluster']==predicted[0]]
    plt.rcParams['figure.figsize']=(20,3)
    for c in cluster_df.drop(['Cluster'],axis=1):
        fig,ax=plt.subplots()
        grid=sns.FacetGrid(cluster_df,col='Cluster')
        grid=grid.map(plt.hist,c)
        plt.show()
        st.pyplot(figsize=(5,5))                   
     
    st.write(cluster_df)
    
    
    
    
    
    
    
    
    
    