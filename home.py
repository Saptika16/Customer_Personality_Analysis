# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 01:57:56 2023

@author: Tina
"""
import streamlit as st

st.set_page_config(page_title='Project',layout='wide')
st.title('This is the Clustering project of team 6 	:books:')
st.markdown('''---''')
st.header(' Customer Personality Analysis :female-technologist:')

st.markdown('''* Customer Personality Analysis is a detailed analysis of a company’s ideal customers. It helps a business to better understand its customers and makes it easier for them to modify products according to the specific needs, behaviors and concerns of different types of customers.
            
* Customer personality analysis helps a business to modify its product based on its target customers from different types of customer segments. For example, instead of spending money to market a new product to every customer in the company’s database, a company can analyze which customer segment is most likely to buy the product and then market the product only on that particular segment.
---
''')
tab1,tab2=st.tabs(['Target',' Attributes :page_facing_up:---'])
with tab2:
    col1,col2=st.columns([1,2])
    attr=col1.radio('Attributes :point_right:',['People','Products','Promotion','Purchase Place'])
    if attr=='People':
        col2.subheader(' People')
        col2.markdown('''
*	ID: Customer's unique identifier
*	Year_Birth: Customer's birth year
*	Education: Customer's education level
*	Marital_Status: Customer's marital status
*	Income: Customer's yearly household income
*	Kidhome: Number of children in customer's household
*	Teenhome: Number of teenagers in customer's household
*	Dt_Customer: Date of customer's enrollment with the company
*	Recency: Number of days since customer's last purchase
*	Complain: 1 if the customer complained in the last 2 years, 0 otherwise
---''')

    elif attr=='Products':
        col2.subheader(' Products')
        col2.markdown('''
*	MntWines: Amount spent on wine in last 2 years
*	MntFruits: Amount spent on fruits in last 2 years
*	MntMeatProducts: Amount spent on meat in last 2 years
*	MntFishProducts: Amount spent on fish in last 2 years
*	MntSweetProducts: Amount spent on sweets in last 2 years
*	MntGoldProds: Amount spent on gold in last 2 years
---''')
    elif attr=='Promotion':
        col2.subheader(' Promotion')
        col2.markdown('''
*	NumDealsPurchases: Number of purchases made with a discount
*	AcceptedCmp1: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
*	AcceptedCmp2: 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
*	AcceptedCmp3: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
*	AcceptedCmp4: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
*	AcceptedCmp5: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
*	Response: 1 if customer accepted the offer in the last campaign, 0 otherwise
---''')
    elif attr=='Purchase Place':
        col2.subheader('Purchase Place')
        col2.markdown('''
*	NumWebPurchases: Number of purchases made through the company’s website
*	NumCatalogPurchases: Number of purchases made using a catalogue
*	NumStorePurchases: Number of purchases made directly in stores
*	NumWebVisitsMonth: Number of visits to company’s website in the last month
---''')
with tab1:
    st.header(' Target  :')
    st.write('Need to perform clustering to summarize customer segments.')





css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.5rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)