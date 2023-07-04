# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 01:57:56 2023

@author: Tina
"""
import streamlit as stm
import pandas as pd


#stm.set_page_config()
stm.set_page_config(page_title='Clustering',layout='wide')
stm.title('This is the Clustering project of team 6')
stm.sidebar.success('Select Any page from here')
stm.write(' 5 Clusters made by KMeans with 59.62% ')
stm.image('5cluster.png')
df_with_cluster=pd.read_csv('df_with_cluster.csv').drop(['Unnamed: 0'],axis=1)
stm.write(df_with_cluster.groupby(['Cluster']).mean().sort_values(['Income'],ascending=False))

stm.markdown('''# Cluster 3 :
* people in 1st cluster of avg age 55 has highest income, saves the most and spends the most are likely to be not a part of family spends most on wine, meat and fish uses discount the least among the clusters to purchase and buys mostly from store doesn't visit website that most (least among all the clusters).

* Accepts any one of any campaign most among all the clusters. 

* Buys the most among all the clusters.

* Uses Discount the least among all the clusters.

* buys from store most among all the clusters

* buys from Catalog the most among all the clusters

* age is doen't matter that much 
 
# cluster 4 :
* people in 2nd cluster of avg age 56 has 2nd highest income, saves the 2nd most and spends the 2nd most are likely to be not a part of family spends most on wine and meat, buys mostly from store doesn't visit website a little more than cluster 1.

* buys from Catalog the most among all the clusters

# cluster 2 :

* buys from website the most among the clusters.

# cluster 5 :

* Uses Discount the most among all the clusters.


# cluster 1 :

* are most likely to be a part of family

* visits the website the most

* buys the least among the clusters
''')