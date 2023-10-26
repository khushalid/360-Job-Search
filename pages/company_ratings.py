#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 03:27:40 2023

@author: harshit nanda
"""

import time
import pandas as pd
import random
import matplotlib.pyplot as plt
import streamlit as st

import os

script_directory = os.path.dirname(os.path.abspath(__file__))


os.chdir(script_directory)

col1, col2, col3 = st.columns(3)

### Reading the data
company_reviews = pd.read_csv("CompaniesFinal.csv")

### Pre-processing the data 

def convert(value):
    if 'T' in value:
        return round(float(value.replace('T', '')) * 1000)
    elif 'L' in value:
        return round(float(value.replace('L', '')) * 100000)
    else:
        return float(value)

# Apply the function to the 'Review' column
company_reviews['Review'] = company_reviews['Review'].apply(convert)

with col1:
    company_name = st.text_input('Enter the Company Name to view Rating', 'None Selected')
    
if "None Selected" in company_name:
    st.table(company_reviews.head(10))

else:
    st.table(company_reviews.loc[company_reviews['Company'] == company_name])
    

### industry plot 
industry_counts = company_reviews['Industry'].value_counts()

# Select the top 10 industries by count
top_10_industries = industry_counts.head(10)

# Create a bar chart
plt.figure(figsize=(10, 6))
ax = top_10_industries.plot(kind='bar', color='skyblue')
plt.xlabel('Industry')
plt.ylabel('Count of Companies')
plt.title('Top 10 Industries by Company Count')

# Display percentages on top of the bars and adjust x-label positions
total = top_10_industries.sum()
for i, count in enumerate(top_10_industries):
    percentage = (count / total) * 100
    ax.text(i, count + 1, f'{percentage:.2f}%', ha='center', va='bottom')

plt.xticks(range(len(top_10_industries.index)), rotation=90)
st.pyplot(plt)  

df = pd.DataFrame(company_reviews)

# Create a histogram of ratings
plt.figure(figsize=(8, 6))
plt.hist(company_reviews['Rating'], bins=5, color='lightblue', edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Count of Companies')
plt.title('Histogram of Ratings by Company Count')
st.pyplot(plt)  

# Create a DataFrame from the data
df = pd.DataFrame(company_reviews)

# Sort the DataFrame by the 'Review' column in ascending order
df_sorted = df.sort_values(by='Review')

# Get the top 5 and bottom 5 companies by number of reviews
top_5 = df_sorted.tail(5)
bottom_5 = df_sorted.head(5)

# Create a bar chart for the top 5 and bottom 5 companies
plt.figure(figsize=(10, 6))
plt.barh(top_5['Company'], top_5['Review'], color='skyblue', label='Top 5')
plt.barh(bottom_5['Company'], bottom_5['Review'], color='lightcoral', label='Bottom 5')
plt.xlabel('Reviews')
plt.ylabel('Company')
plt.title('Top 5 and Bottom 5 Companies by Number of Reviews')
plt.legend()
plt.gca().invert_yaxis()

# Add data labels for reviews
for index, value in enumerate(top_5['Review']):
    plt.text(value, index, str(value), va='center', color='black', fontsize=10)

for index, value in enumerate(bottom_5['Review']):
    plt.text(value, index + 5, str(value), va='center', color='black', fontsize=10)

st.pyplot(plt)  


# Create a DataFrame from the data
df = pd.DataFrame(company_reviews)

# Calculate the distribution of company count by employee size
employee_size_counts = df['Employee_Size'].value_counts()
total_companies = len(df)
employee_size_percentages = (employee_size_counts / total_companies) * 100

# Create a pie chart
plt.figure(figsize=(8, 8))
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
plt.pie(employee_size_percentages, labels=employee_size_percentages.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Employee Size vs Company Count (Percentage)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(plt) 
    


    
    

