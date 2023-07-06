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
myTable=pd.read_csv('myTable.csv')
stm.title('Cluster Analysis')
stm.markdown('---')
tab1, tab2,tab3 =stm.tabs(['Clusters 	:card_file_box:','Cluster Analysis :robot_face:','Conclusion :memo:'])


with tab1:
    stm.image('5cluster.png',width=700)
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