# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 02:41:52 2023

@author: Tina
"""
import streamlit as stm
import pandas as pd


#stm.set_page_config()stm.set_page_config(page_title='Clustering',layout='wide')
stm.set_page_config(page_title='clustering',layout='wide')
df_with_cluster=pd.read_csv('df.csv')
myTable=pd.read_csv('myTable.csv').drop(['Unnamed: 0'],axis=1)
stm.title('Cluster Analysis')
stm.markdown('---')
tab1, tab2,tab3 =stm.tabs(['Clusters 	:card_file_box:','Cluster Analysis :robot_face:','Conclusion :memo:'])


with tab1:
    col1,col2=stm.columns([1,1])
    col1.image('5cluster.png')
    col2.markdown('''
                  Cluster 0 = 1st cluster = Lowest economic Class
                  
                  Cluster 1 = 2nd cluster = Highest economic Class
                  
                  Cluster 2 = 3rd cluster = Lower Middle Class
                  
                  Cluster 3 = 4th cluster = Upper Middle Class
                  
                  Cluster 4 = 5th cluster = Low economical Class
                  
                  ''')
    #col1.image('cluster_scatter.png')
    stm.write(df_with_cluster.groupby(['Cluster']).mean().sort_values(['Income'],ascending=False))
with tab2:
    stm.subheader('Clusters sorted based on Income')
    stm.write(df_with_cluster.groupby(['Cluster']).mean().sort_values(['Income'],ascending=False))
    stm.write(myTable)
        
with tab3:
    col1,col2=stm.columns([1,2])
    col1.image('cluster_scatter.png')
    col2.markdown('''
                 * 2nd Cluster is the cluster with high end values which is indicating that this cluster has very high end peple who are rare.
                
                 * 4th cluster are people who are well to do
                 
                 * 3rd and 5th indicates average financial stable people
                 
                 * 1st cluster indicates people who are not so well to do
                 ''')
    col2.markdown('''
                  Cluster 0 = 1st cluster = Lowest economic Class
                  
                  Cluster 1 = 2nd cluster = Highest economic Class
                  
                  Cluster 2 = 3rd cluster = Lower Middle Class
                  
                  Cluster 3 = 4th cluster = Upper Middle Class
                  
                  Cluster 4 = 5th cluster = Low economical Class
                  
                  ''')                 