# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:55:11 2023

@author: Tina
"""
import streamlit as st

st.set_page_config(page_title='EDA',layout='wide')
st.title('Exploratory Data Analysis :bar_chart:')
st.divider() 
column1, column2 = st.columns([1,2])
with column1:
    eda=st.radio('EDA related to:',
                 ['Products','Purchase Place',
                  'Campaign','Economic Status','Family Dynamics'])

with column2:
    if eda=='Products':
        prod=st.selectbox('Product related EDA ',
                          ['Product Outliers','Expenditure~Products',
                           'Expenditure~Income~Marital Status',
                           'Total Expenditure',
                           'Wine Purchase based on kids and education',
                           'Wine Purchase based on teens and education',
                           'Expenditure on sweet if there are kids',
                           'Expenditure on sweet if there are teens'])
        col1,col2=st.columns([1,2])
        
        if prod== 'Expenditure~Products':
            with col2:
                st.image('expenditure_prod_all.png')
            with column1:
                st.markdown('* We observed that customer is spending more on meat and wine')
        elif prod=='Wine Purchase based on kids and education':
            with col2:
                st.image('wine_kid_education.png')
            with column1:
                st.markdown('graduated people are the only people who have kids still they are spending on wine')
        elif prod=='Wine Purchase based on teens and education':
             with col2:
                 st.image('wine_teen_education.png')
             with column1:
                 st.markdown('more number of kids at home reduces the sweet buyers')
                 
        elif prod=='Expenditure on sweet if there are teens':
             with col2:
                 st.image('teen_sweet.png')
             with column1:
                 st.markdown('as teens at home increases buying sweet items reduces')

                 
        elif prod=='Expenditure on sweet if there are kids':
             with col2:
                 st.image('sweet_kid.png')
             with column1:
                 st.markdown('graduated people are the only people who have kids still they are spending on wine')
                 
               
        elif prod=='Product Outliers':
            with col2:
                st.image('eda_exp_prod_outliers.png')
            with column1:
                st.markdown('''# Inference:

* Wine:
Amount spent by the customers on wine ranges the most , people spent much more on wine than the rest of the items

* Fruits:
customer used to spent least on fruits

* Meat:
customer used to spent on meat that is not that more but there are few outliers with might indicate that there are few meat products which are very high priced . Maybe during occations special types of meat products needed to bought.

* Fish:
customer used to spent on fish items is fairly not more than rest of the items

* Sweets:
again they spent far too less on sweets

* Gold: they spent on gold is on an average not that much compared to wine

* Inference :
* Customer spends more on wine''')
        elif prod=='Expenditure~Income~Marital Status':
            with col2:
                st.image('eda_exp_prod_mar.png')
            with column1:
                st.markdown('* We observed that customer is spending more on meat and wine')
    
        elif prod=='Total Expenditure':
            with col2:
                st.image('eda_total_exp.png')
            with column1:
                st.markdown('''* wine is the most spend on product and fruit is the least bought product ''')
        
    elif eda=='Purchase Place':
        purchase=st.selectbox('Expenditure from different places related EDA ',
                            ['Age effecting the purchase','Discount Timeline',
                             'purchase made by elderly people',
                             'purchase made by middle aged people',
                             'purchase made by young people','Total Purchases from different places','Website visit last month'])
       
        if purchase== 'Age effecting the purchase':
            with column2:
                st.image('eda_exp_age_purchase.png')
            with column1:
                st.markdown('---')
                st.markdown('')
        elif purchase=='Discount Timeline':
            with column2:
                st.image('eda_timeline_discount.png')
            with column1:
                st.markdown('---')
                st.markdown('')
                
        elif purchase=='purchase made by elderly people':
            with column2:
                st.image('eda_pur_elderly.png')
            with column1:
                st.markdown('---')
                st.markdown('''* Elderly ones buy mostly from stores''')
                
        elif purchase=='purchase made by middle aged people':
            with column2:
                st.image('eda_pur_middleage.png')
            with column1:
                st.markdown('---')
                st.markdown('''* Middle Aged ones buy mostly from stores''')
                
        elif purchase=='purchase made by young people':
            with column2:
                st.image('eda_pur_young.png')
            with column1:
                st.markdown('---')
                st.markdown('''* Young ones buy mostly from stores''')
                
     
        elif purchase=='Total Purchases from different places':
            with column2:
                st.image('eda_purplace.png')
            with column1:
                st.markdown('---')
                st.markdown('''* People buy things mostly from store ''')
                
     
        elif purchase=='Website visit last month':
            with column2:
                st.image('eda_webvisit.png')
            with column1:
                st.markdown('---')
                st.markdown('''* as teens increases expenditure decreases''')
                
     


        
        
        
    elif eda=='Campaign':
        campaign=st.selectbox('Campaign accepted by customers related EDA ',
                            ['Accepted Campaign',
                             'Campaign accepted if teens are there in home',
                             'Campaign accepted if kids are there in home',
                             'Campaign accepted ~ Marital Status','Recency of customers ~ Years Enrolled'])
        
        if campaign== 'Accepted Campaign':
            with column2:
                st.image('accepted_camp.png')
            with column1:
                st.markdown('---')
                st.markdown('* 4th campaign was the most successful campaign')
        elif campaign=='Campaign accepted if teens are there in home':
            with column2:
                st.image('camp_teens.png')
            with column1:
                st.markdown('---')
                st.markdown('''* people who has no teen accepts campaigns''')
                
        elif campaign=='Campaign accepted if kids are there in home':
            with column2:
                st.image('camp_kids.png')
            with column1:
                 st.markdown('---')
                 st.markdown('''* people who has no kid accepts campaigns ''')
                
      
        elif campaign=='Campaign accepted ~ Marital Status':
            with column2:
                st.image('camp_mar_status.png')
            with column1:
                st.markdown('---')
                st.markdown('''* married people accepts the campaign the most''')
                
     
        elif campaign=='Recency of customers ~ Years Enrolled':
            with column2:
                st.image('eda_recency_years.png')
            with column1:
                 st.markdown('---')
                 st.markdown('''*  Who have recently enrolled are more recent buyers''')
                 
         
        
    
        
    elif eda=='Economic Status':
        eco_st=st.selectbox('Expenditure based on Economic Status related EDA ',
                            ['Savings made by people of different economic status',
                             'economic status count','Income of each economic staus',
                             'complains made by people of different economic status',
                             'expenditure made by people of different economic status',
                             'Buying Capacity'])
        if eco_st== 'Savings made by people of different economic status':
            with column2:
                st.image('economic_savings_bar.png')
            with column1:
                st.markdown('---')
                st.image('economic_savings.png')
                st.markdown('* upper middle saves the most')
        elif prod=='Buying Capacity':
            with col2:
                st.image('eda_buying_capacity.png')
            with column1:
                st.markdown(''' ''')
                
        elif eco_st=='economic status count':
            with column2:
                st.image('economic_st_count.png')
            with column1:
                st.markdown('---')
                st.markdown('''* Mostly there are Lower middle Economic status category ''')
                
        elif eco_st=='complains made by people of different economic status':
            with column2:
                st.image('economic_st_complain.png')
            with column1:
                 st.markdown('---')
                 st.image('economic_st_complain_line.png')
                 st.markdown('''* status 2 i.e., Lower middle Economic status complains the most and high economic people don't complain at all
                             * Above two plots explains that status 1 peole with salary range of 8119.85  to  40599.25 complains the most and who has the maximum salary of status 4 complains the least''')
                 
        elif eco_st=='expenditure made by people of different economic status':
            with column2:
                st.image('eda_exp_eco_st.png')
            with column1:
                  st.markdown('---')
                  st.markdown('''* status 3 : Upper middle people spend the most ''')
                  
        elif eco_st=='Income of each economic staus':
            with column2:
                st.image('eco_st_income.png')
            with column1:
                   st.markdown('---')
                   st.markdown('''* as the status increases the income increases ''')
                  
      
        
    elif eda=='Family Dynamics':
        family=st.selectbox('Family Dynamics related EDA ',
                            ['Expenditure if there are kids in home',
                             'Expenditure if there are teens in home',
                             'Expenditure based on Marital Status',
                             'Relation Status','Education',
                             'Expenditure based on degree','Enrollment based on age and marital status'])
        col1,col2=st.columns([2,1])
        with col2:
            st.write('       ')
        if family== 'Expenditure if there are kids in home':
            with col1:
                st.image('eda_exp_kid.png')
            with column1:
                st.markdown('---')
                st.image('eda_exp_kids_line.png')
                st.markdown('* as no of kids at home increases expenditure decreases')
        elif family=='Expenditure if there are teens in home':
            with col1:
                st.image('eda_exp_teens.png')
            with column1:
                st.markdown('---')
                st.markdown('''* as teens increases expenditure decreases''')
                st.image('eda_exp_teens_line.png')
        elif family=='Enrollment based on age and marital status':
            with col1:
                st.image('mar_enr_age.png')
            with column1:
                st.markdown('''* Married people are mostly enrolled for 10 years as well as single people...most people are enrolled for 10 years''')
       
        
        elif family=='Expenditure based on Marital Status':
            with col1:
                st.image('eda_exp_mar_st.png')
            with column1:
                st.markdown('''* expenditure increases as people are together or married''')
        elif family=='Relation Status':
            with col1:
                st.image('eda_marital_st.png')
            with column1:
                st.markdown('''* mostly there are married people ''')
        elif family=='Education':
            with col1:
                st.image('education.png')
            with column1:
                st.markdown('''* mostly there are graduates''')
        elif family=='Expenditure based on degree':
            with col1:
                st.image('eda_total_exp_degree.png')
            with column1:
                st.markdown('''*  Conclusion: 
* we can say that Graduates are people who spends most''')
               
        
        
        
        
        