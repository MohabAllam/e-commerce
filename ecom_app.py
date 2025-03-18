
# Import Necessary Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide", page_title = 'Simple DashBoard')

# Read Data
df = pd.read_csv('cleaned_df.csv', index_col= 0)

# st.title('Ecommerce Data Analaysis Project')

# Create title using html
html_title = """<h1 style="color:white;text-align:center;"> Ecommerce Data Analaysis Project </h1>"""
st.markdown(html_title,unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(['Home Page', 'Univariate Analysis', 'Bivariate Analysis'])

# Home Page
tab1.image('ecommerce.jpg')

tab1.write('### Data Sample')
tab1.dataframe(df.head())

# Univariate
for col in df.columns:

    tab2.plotly_chart(px.histogram(df, x = col, title= col))

# Bivariate
tab3.write('### What is the total number of orders per Country ?')
country_count = df.Country.value_counts()
tab3.plotly_chart(px.bar(country_count, x= country_count.index, y= country_count.values, title= 'Number of Transactions per Country', 
                                                                       labels= {'Country' : 'All Countries', 'y' : 'No of Transactions'}))

tab3.write('### What is the total number of orders per Minor Category ?')
minor_count = df['Minor Category'].value_counts()
tab3.plotly_chart(px.bar(minor_count, x= minor_count.index, y= minor_count.values, title= 'Number of Orders per Minor Category',
                                                                 color_discrete_sequence= ['#ed7953'],
                                                                 labels= {'y' : 'No of Orders'}))           


col1, col2 = tab3.columns(2, vertical_alignment= 'center')

col1.write('### What is the distribution of order value over the time ?')
df_sorted = df.sort_values(by= 'InvoiceDateTime')
col2.plotly_chart(px.line(df_sorted, x= 'InvoiceDateTime', y= 'OrderValue', height= 400, width = 1200))
