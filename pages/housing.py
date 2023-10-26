#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:49:04 2023

@author: tirthparekh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import seaborn as sns
import time
import argparse
import re
import warnings
import copy
from pandas.plotting import table
import streamlit as st
warnings.filterwarnings('ignore')


# housing_data = pd.read_csv('airbnb_data.csv')
# housing_data_sf = pd.read_csv('sf_airbnb.csv')

# housing_data['neighborhood_overview'].fillna('Not Present', inplace = True)
# housing_data_sf['neighborhood_overview'].fillna('Not Present', inplace = True)
# housing_data.fillna(0, inplace = True)
# housing_data_sf.fillna(0, inplace = True)
# housing_data['bathrooms_text'] = housing_data['bathrooms_text'].str.extract(r'(\d+)')
# housing_data.drop('bathrooms', axis = 1, inplace = True)
# housing_data.rename(columns={'bathrooms_text': 'bathrooms'}, inplace=True)

# list_of_columns = ['id','listing_url','name','description','neighborhood_overview','accommodates','bathrooms','bedrooms','beds','amenities','price','review_scores_value','city']

# housing_data = housing_data[list_of_columns]
# housing_data_sf = housing_data_sf[list_of_columns]
# housing_data_final = pd.concat([housing_data,housing_data_sf], ignore_index=True)

# housing_data_final.to_csv('airbnb_data_final.csv', index = False)




#price_range_low = 0
#price_range_high = 1000
#number_of_accomodates = 3
#number_of_bedrooms = 2
#number_of_bathrooms = 1
amenities = ['Hangers', 'Wifi']
#city = 'Boston'
sort_by = 'review_scores_value'

location_list = ['Boston', 'Chicago', 'San Francisco']

group_by_list = ['city', 'accommodates', 'bedrooms']

value_by_list = ['price', 'review_scores_value']

col1,col2, col3, col4 = st.columns(4)

col5,col6, col7, col8 = st.columns(4)


with col1:
    input_city = st.multiselect('Select the city:', ['Select All'] + location_list, default=['Select All'])
with col2:
    min_price = st.text_input('Enter the lowest price', 0)
with col3:
    max_price = st.text_input('Enter the highest price',1000)
with col4:
    grouping_columns = st.multiselect('Select the grouping columns:', ['Select All'] + group_by_list, default=['city'])
with col5: 
    num_accomodates = st.text_input('Enter the no. of accomodates', 1)
with col6: 
    num_bedrooms = st.text_input('Enter the minimum no. of bedrooms', 1)
with col7: 
    num_bathrooms = st.text_input('Enter the minimum no. of bathrooms', 1)
with col8: 
    grouping_value_columns = st.multiselect('Select the grouping value columns:', ['Select All'] + value_by_list, default=['Select All'])
    
if "Select All" in input_city:
    input_city = location_list
    
if "Select All" in grouping_columns:
    grouping_columns = group_by_list

if "Select All" in grouping_value_columns:
    grouping_value_columns = value_by_list
    
city = input_city
price_range_low = min_price
price_range_high = max_price
number_of_accomodates = num_accomodates
number_of_bedrooms = num_bedrooms
number_of_bathrooms = num_bathrooms

housing_data_complete = pd.read_csv('airbnb_data_final.csv')
housing_data_complete['price'] = housing_data_complete['price'].str.replace('$','')
housing_data_complete['price'] = housing_data_complete['price'].str.replace(',','')
housing_data_complete['amenities'] = housing_data_complete['amenities'].str.replace('[^a-zA-Z, ]','', regex=True)
housing_data_complete = housing_data_complete[housing_data_complete['bedrooms'] != 0.0]
housing_data_complete = housing_data_complete[housing_data_complete['beds'] != 0.0]
housing_data_complete['neighborhood_overview'] = housing_data_complete['neighborhood_overview'].str.replace('[^a-zA-Z0-9,. ]', '', regex=True)
housing_data_complete['description'] = housing_data_complete['description'].str.replace('[^a-zA-Z0-9,. ]', '', regex=True)
housing_data_complete.fillna(0, inplace = True)
housing_data_complete = housing_data_complete.sort_values(by='bedrooms', ascending = False)

housing_data_complete['price'] = housing_data_complete['price'].astype(float)
housing_data_complete['accommodates'] = housing_data_complete['accommodates'].astype(float)
housing_data_complete['bathrooms'] = housing_data_complete['bathrooms'].astype(float)
housing_data_complete['bedrooms'] = housing_data_complete['bedrooms'].astype(float)
housing_data_complete['review_scores_value'] = housing_data_complete['review_scores_value'].astype(float)

def fill_zero_with_random_int(x):
    if x == 0:
        return np.random.randint(0, 11)
    return x

housing_data_complete['review_scores_value'] = housing_data_complete['review_scores_value'].apply(fill_zero_with_random_int)


user_request_data = housing_data_complete[(housing_data_complete['price'] > float(price_range_low)) 
                                        & (housing_data_complete['price'] <= float(price_range_high))
                                        & (housing_data_complete['accommodates'] >= float(number_of_accomodates))
                                        & (housing_data_complete['city'].isin(city))
                                        & (housing_data_complete['bathrooms'] >= float(number_of_bathrooms))
                                        & (housing_data_complete['bedrooms'] >= float(number_of_bedrooms))]
columns_for_group_by = ['city','accommodates', 'bedrooms', 'price', 'review_scores_value']
average_table_data = user_request_data[columns_for_group_by]

user_request_data = user_request_data.sort_values(by=['review_scores_value','price'], ascending = [False,True])

user_request_data_head = copy.deepcopy(user_request_data.head(10))

def insert_line_break(text, max_width):
    words = text.split()
    lines = []
    current_line = ''
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_width:
            if current_line:
                current_line += ' '
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return '\n'.join(lines)

columns_to_display = ['listing_url', 'name', 'description','neighborhood_overview', 'accommodates', 'bedrooms','bathrooms','amenities','price','review_scores_value']
user_request_data_head = user_request_data_head[columns_to_display]
user_request_data_head['description'] = user_request_data_head['description'].apply(lambda x: insert_line_break(x, max_width=55))
user_request_data_head['neighborhood_overview'] = user_request_data_head['neighborhood_overview'].apply(lambda x: insert_line_break(x, max_width=55))
user_request_data_head['name'] = user_request_data_head['name'].apply(lambda x: insert_line_break(x, max_width=20))
user_request_data_head['amenities'] = user_request_data_head['amenities'].apply(lambda x: insert_line_break(x, max_width=45))
user_request_data_head['listing_url'] = user_request_data_head['listing_url'].str.replace('.com/','.com/\n', regex = True )
user_request_data_head = user_request_data_head.reset_index(drop=True)


# Define custom CSS styles for the table
styles = [
    {'selector': 'td', 'props': [('font-size', '16px'), ('text-align', 'center')]},
    {'selector': 'th', 'props': [('font-size', '18px'), ('text-align', 'center')]},
    {'selector': '.data', 'props': [('font-size', '14px'), ('text-align', 'center')]},
]

fig, ax = plt.subplots(figsize=(9, 4))

price_visualization_data = pd.DataFrame(user_request_data['price'])

# Define the price ranges and bins
price_ranges = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Create a histogram-like bar plot
ax.hist(price_visualization_data['price'], bins=price_ranges, color='lightblue', edgecolor='black', alpha=0.7)
ax.set_xlabel('Price Range')
ax.set_ylabel('Number of Houses')
plt.title('Price Range Distribution')

st.pyplot(fig)

reviews_visualization_data = pd.DataFrame(user_request_data['review_scores_value'])

grouped = reviews_visualization_data['review_scores_value'].value_counts()

fig, ax = plt.subplots()
ax.pie(grouped, labels=None, autopct='', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

legend_labels = [f'{label} ({percentage:.1f}%)' for label, percentage in zip(grouped.index, grouped / grouped.sum() * 100)]
plt.legend(legend_labels, title='Distribution of Reviews', loc='upper left', bbox_to_anchor=(1, 1))

plt.title('Distribution of Reviews')

st.pyplot(fig)

grouped_avg_price_reviews = average_table_data.groupby(grouping_columns)[grouping_value_columns].mean().reset_index()
#grouped_avg_price_reviews = grouped_avg_price_reviews.sort_values(by=[grouping_value_columns], ascending = [False])
st.markdown("<h3 style='text-align: center;'>House Listings grouped by selections on Average price per reviews</h3>", unsafe_allow_html=True)
st.table(grouped_avg_price_reviews)

st.markdown("<h3 style='text-align: center;'>Top 10 House Listings with Best Reviwes and Lowest prices</h3>", unsafe_allow_html=True)
st.table(user_request_data_head)




