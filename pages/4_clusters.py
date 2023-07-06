# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 02:41:52 2023

@author: Tina
"""
import streamlit as stm
import pandas as pd
from prettytable import PrettyTable

#stm.set_page_config()stm.set_page_config(page_title='Clustering',layout='wide')
stm.set_page_config(page_title='clustering',layout='wide')
df_with_cluster=pd.read_csv('df.csv')
stm.title('Cluster Analysis')
stm.markdown('---')
tab1, tab2,tab3 =stm.tabs(['Clusters 	:card_file_box:','Cluster Analysis :robot_face:','Conclusion :memo:'])


#specify the column name while initializing the table
myTable=PrettyTable(['','Feature','2nd Cluster','4th Cluster','3rd Cluster','5th Cluster','1st Cluster'])
#add rows
myTable.add_row(['1','age','','','','Oldest','Youngest'])
myTable.add_row(['2','Family','not that much chance of being a part of family','least chances of being a part of family','3rd highest chance of being a part of family','very high chance of being a part of family','2nd most likely to be part of family'])
myTable.add_row(['3','Income','highest','higher','high','low','lowest'])
myTable.add_row(['4','Total Purchases from store/website/catalog','highest','higher','high','low','lowest'])
myTable.add_row(['5','Accepting Campaigns','accepts the most','2nd most likely to accept','4th most likely to accept','3rd most likely to accept','least chance'])
myTable.add_row(['6','Expenditure','highest','higher','high','low','lowest'])
myTable.add_row(['7','Savings','highest','higher','high','low','lowest'])
myTable.add_row(['8','economic status','highest','higher','high','low','lowest'])
myTable.add_row(['9','Kids at home','','least chance of having kids at home','','','highest chance of having kids'])
myTable.add_row(['10','Teens at home','','least chance of having teens','','highest chance of having teens at home ',''])
myTable.add_row(['11','Recency','Youngest','','','','Oldest'])
myTable.add_row(['12','Expenditure on Wine','highest','higher','high','low','lowest'])
myTable.add_row(['13','Expenditure on Fruits','higher','highest','high','low','lowest'])
myTable.add_row(['14','Expenditure on Meat','higher','highest','high','low','lowest'])
myTable.add_row(['15','Expenditure on Fish','higher','highest','high','low','lowest'])
myTable.add_row(['16','Expenditure on Sweets','higher','highest','high','low','lowest'])
myTable.add_row(['17','Expenditure on Gold','higher','highest','high','low','lowest'])
myTable.add_row(['18','Discount used to Purchase','very rarely','doesnt use discount to purchase that much and least among all the clusters','higher','highest','high'])
myTable.add_row(['19','Web Purchase','highest in buying online','4th','3rd highest','2nd highest','lowest among the clusters '])
myTable.add_row(['20','Catalog Purchase','buys most','2nd most buyer','3rd most','4th most','lieast likely to buy'])
myTable.add_row(['21','Store Purchase','3rd most likely','highest chance','2nd most likely','4th','least likely'])
myTable.add_row(['22','Website visit last month','3rd most likely to visit','visits the most','2nd to visit','4th','visits the least'])
myTable.add_row(['23','Campaign 1','accepts the most','2nd','4th','3rd',"does't accept"])
myTable.add_row(['24','Campaign 2','accepts the most',"does't accept","does't accept",'',"does't accept"])
myTable.add_row(['25','Campaign 3','accepts the most','4th','accepts the least','2nd','3rd'])
myTable.add_row(['26','Campaign 4','accepts the most','4th','3rd','2nd','least'])
myTable.add_row(['27','Campaign 5','accepts the most','2nd','3rd','4th',"does't accept"])
myTable.add_row(['28','Response for last campaign','Accepts the most','3rd','4th','2nd most likely to accepts','least'])
myTable.add_row(['29','Complain','4th','complains the least','complains the most','3rd','2nd'])

with tab1:
    stm.image('5cluster.png',width=700)
    #col1.image('cluster_scatter.png')
    stm.write(df_with_cluster.groupby(['Cluster']).mean().sort_values(['Income'],ascending=False))
with tab2:
    stm.subheader('Clusters sorted based on Income')
    stm.write(df_with_cluster.groupby(['Cluster']).mean().sort_values(['Income'],ascending=False))
    myTable
        
with tab3:
    col1,col2=stm.columns([1,2])
    col1.image('cluster_scatter.png')
    col2.markdown('''
                 * 2nd Cluster is the cluster with high end values which is indicating that this cluster has very high end peple who are rare.
                
                 * 4th cluster are people who are well to do
                 
                 * 3rd and 5th indicates average financial stable people
                 
                 * 1st cluster indicates people who are not so well to do
                 ''')