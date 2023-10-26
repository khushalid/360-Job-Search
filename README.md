# 360-Job-Search
360 Job Hunt Portal is a one stop platform which gives user information on Jobs available, Companies, Company Ratings, Housing details in a few locations and the Courses that are available and employees look into to prepare for company interviews.

Our portal has various tabs where the user can navigate through and look through the data and visualizations, which give the user a good idea around each aspect of job search.

For this project, we have limited our data to 3 cities in United States:

Boston
Chicago
San Francisco

Datasets Formation

Datasets formed by scraping LinkedIn:

LinkedIn_Data_Scientist_Boston.csv 
LinkedIn_Data_Scientist_Chicao.csv
LinkedIn_Data_Scientist_San_Francisco.csv
LinkedIn_Software_Engineer_Boston.csv
LinkedIn_Software_Engineer_Chicago.csv
LinkedIn_Software_Engineer_San_Francisco.csv
	
We concatenate all these datasets in a dataframe, clean and perform visualizations


Dataset formed by scraping Coursera
Coursera_Courses_test.csv

Housing dataset collected from Kaggle
Airbnb_data_final.csv

Dataset formed by scraping Glassdoor
CompanyList.csv

We have used streamlit to integrate the backend data and eventually display the visualizations from the data to frontend. We have made an interactive portal where user can enter values and data is filtered and visualized accordingly. 



Executing the code:

We are using streamlit to host the code, that is when the code is run using streamlit a web page will pop up which will be the 360 Job Hunt Portal.

Note: Make sure Google chrome is present on the system, We are using selenium webdriver to scrape linkedIn data. 


Below are the steps to execute the code:

Uploaded is a zip file, main.zip, extract it.
Inside main.zip, there is a file requirements.txt
Execute command below to install all the necessary libraries for running the project
pip install -r requirements.txt
Important libraries needed to run the project are: pandas, numpy, matplotlib, selenium, beautifulSoup, streamlit, plotly, requests.
Once installation is complete run the below command to start the application
streamlit run main.py
This will start a localhost and open a new browser tab on the system where you should see the project up and running. If it doesnt open automatically, on execution streamlit run on the terminal you will see a localhost link, manually copy that and run in the browser. The project should run



Navigating through the project:

On running the project, the first page that will open will be the Job Hunt Portal main page.

Main Job Hunt Portal

This is the main page, which will welcome you to the Portal. It has an overall overview of all the aspects related to job hunting, visualizations which will give the user an overview of the Company Average salaries based on Industries, Job Roles, Housing prices, Company ratings etc.

You can navigate to different pages from the sidebar.

Below are the descriptions of the python files and short description of the portal functionalities and navigations:

main.py file:

This file first imports all the datasets that are formed by Scraping or found on the internet. We clean the datasets first, and then we use it to perform analytics and visualization. This file mainly consists of aggregation of the datasets and then performing visualizations on aggregated data. 

Company_Ratings.py file

This file is an interactive dashboard for displaying visualizations about company ratings, reviews and details. For this file we use the glassdoor data scraped into csv file CompanyList.csv. 

Coursera_Scrapings.py file:

This file has a button which when clicked triggers the scraping of coursera website (which is used to make courses dataset) and will scrape data from coursera and store it into a csv file.

Courses.py file

This file is an interactive dashboard for displaying visualizations and details for various courses, domains of courses, course organizations and ratings for each course such that the user can know which courses he should take to prepare for the interviews in the domain of job he/she is applying to. It uses the dataset generated from coursera – Coursera_Courses_test.csv

Housing.py

This file uses the housing dataset which was taken from kaggle, which contains the details of rent, location, price, neighborhood, location, amenities, accommodates, reviews etc. This data was cleaned, filtered and preprocessed to generate data on which visualizations can be performed. It uses the dataset - airbnb_data_final.csv

Job_Search.py

This file generates an interactive dashboard for available job postings on LinkedIn and uses datasets which were made by scraping LinkedIn Jobs. Since we scrape data from LinkedIn individually based on Job Role and City we eventually concatenate all the datasets to generate a common dataset on which preprocessing and cleaning is performed to eventually generate visualizations and provide information the user needs.

LinkedIn_Scraping.py

This file is used to manually trigger scraping of LinkedIn to generate the datasets for jobs available on LinkedIn platform. There are 6 buttons provided on the screen which are used to trigger web scraping for the specific option selected.

Company_Review_Scraping.py

This file is used to manually trigger scraping of Glassdoor to generate a dataset which contains company review and ratings. A button is provided on the screen to trigger the scraping for Glassdoor, once completed a dataset ‘CompanyList.csv’ is generated.
