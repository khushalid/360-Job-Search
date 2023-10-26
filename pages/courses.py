#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 04:49:00 2023

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
import streamlit as st
warnings.filterwarnings('ignore')
import os

script_directory = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_directory)

courses = pd.read_csv('Coursera_Courses_test.csv')
course_organization = courses['course organization'].unique().tolist()
course_skills = courses['course skills'].unique().tolist()

col1,col2, col3 = st.columns(3)

course_skills_with_select_all = ["Select All"] + course_skills

course_organization_with_select_all = ["Select All"] + course_organization


with col1:
    course_skills_input = st.multiselect('Select the Course Skills:', course_skills_with_select_all, default = ['Select All'])
with col2:
    course_organizarion_input = st.multiselect('Enter the Course Organization', course_organization_with_select_all, default = ['Select All'])
with col3: 
    min_rating = st.text_input('Enter the Min Rating', 0)

if "Select All" in course_organizarion_input:
    course_organizarion_input = course_organization
    
if "Select All" in course_skills_input:
    course_skills_input = course_skills

courses = courses[(courses['course rating'] >= float(min_rating))
                      & (courses['course skills'].isin(course_skills_input))
                      & (courses['course organization']).isin(course_organizarion_input)]

st.markdown("<br>", unsafe_allow_html=True) 

# grouped = courses['course skills'].value_counts()

# fig, ax = plt.subplots()
# ax.pie(grouped, labels=None, autopct='', startangle=90)
# ax.axis('equal')

# legend_labels = [f'{label} ({percentage:.1f}%)' for label, percentage in zip(grouped.index, grouped / grouped.sum() * 100)]
# plt.legend(legend_labels, title='Distribution of Industries', loc='upper left', bbox_to_anchor=(1, 1))

# plt.title('Distribution of Course skills')

# st.pyplot(fig)

review_ranges = [1,1.5,2,2.5,3,3.5,4,4.5,5]
fig, ax = plt.subplots()
n, bins, patches = ax.hist(courses['course rating'], bins=review_ranges, edgecolor='k', alpha=0.75)


counts = [int(count) for count in n]

# Annotate each bar with its count
for count, x, patch in zip(counts, bins, patches):
    ax.text(x + (bins[1] - bins[0]) / 2, count, str(count), ha='center', va='bottom')


ax.set_xlabel('Reviews')
ax.set_ylabel('Count')
ax.set_title('Courses Rating Range')

st.pyplot(fig)

st.markdown("<br>", unsafe_allow_html=True) # This adds a space
columns_for_table = ['course title','course URL','course organization', 'course skills', 'course rating']
courses_data_table = courses[columns_for_table]

courses_data_table = courses_data_table.sort_values(by=['course rating'], ascending = [False])

st.table(courses_data_table.head(10))

