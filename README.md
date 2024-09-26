![image](https://github.com/NazriJasmal/Data-Science-Intern-at-Data-Glacier/assets/141367755/c7b0e4f0-d30c-47d9-9a56-27bd9824bcd0)

## Week 1- Version Control Assignment

Clone the VC repo (https://github.com/DataGlacier/VC.git)
Create a new branch
checkout newly created branch
Run the add.py and provide your name and fav sport as input
Run the test script using below command:      
pytest test/test.py -s
ignore warning and if there is no error then add,commit and push your changes to repo

## Week 2- Project: G2M insight for Cab Investment firm & Week 3- Presentation of the Project

The Client XYZ is a private firm in US. Due to remarkable growth in the Cab Industry in last few years and multiple key players in the market, it is planning for an investment in Cab industry and as per their Go-to-Market(G2M) strategy they want to understand the market before taking final decision.

#### Project delivery:

You have been provided with multiple data sets that contains information on 2 cab companies. Each file (data set) provided represents different aspects of the customer profile. XYZ is interested in using your actionable insights to help them identify the right company to make their investment.

The outcome of your delivery will be a presentation to XYZ’s Executive team. This presentation will be judged based on the visuals provided, the quality of your analysis and the value of your recommendations and insights. 

#### DataSet: https://drive.google.com/drive/folders/1peKiUDP95iv7IjBn0T5jcRHDW7Ezu9OQ

You have been provided 4 individual data sets. Time period of data is from 31/01/2016 to 31/12/2018.

Below are the list of datasets which are provided for the analysis:

Cab_Data.csv – this file includes details of transaction for 2 cab companies

Customer_ID.csv – this is a mapping table that contains a unique identifier which links the customer’s demographic details

Transaction_ID.csv – this is a mapping table that contains transaction to customer mapping and payment mode

City.csv – this file contains list of US cities, their population and number of cab users

#### Tasks

You should fully investigate and understand each data set.

Review the Source Documentation

Understand the field names and data types

Identify relationships across the files

Field/feature transformations

Determine which files should be joined versus which ones should be appended

Create master data and explain the relationship

Identify and remove duplicates

Perform other analysis like NA value and outlier detection

Prepare a presentation that summarizes your analysis and recommendations and identify which company is performing better and is a better investment opportunity for XYZ.
Whatever and how many slides you prepare(Be creative and come up with meaningful insight)

## Week4: Deployment on Flask

#### Task:

1. Select any toy data (simple data).

2. Save the model

3. Deploy the model on flask ( web app)

4. Create pdf document (Name, Batch code, Submission date, Submitted to ) which should contain snapshot of each step of deployment)

5. Upload the document to Github

6. Submit the URL of the uploaded document.

## Week 5: Cloud and API deployment

#### Task:

1. Select any toy data (simple data) ( You are allowed to use data set of week 4)

2. Save the model ( You are allowed to use model of week 4)

3. Deploy the model on any cloud eg: Heroku,AWS,GCP,Azure (Deployment should be API based as well as web app)

4. Create pdf document (Name, Batch code, Submission date, Submitted to ) which should contain snapshot of each step of deployment)

5. Upload the document and code to Github

6. Submit the URL of the uploaded document.

## Week 6: File ingestion and schema validation

#### Task:

Take any csv/text file of 2+ GB of your choice. --- (You can do this assignment on Google colab)

Read the file ( Present approach of reading the file )

Try different methods of file reading eg: Dask, Modin, Ray, pandas and present your findings in term of computational efficiency

Perform basic validation on data columns : eg: remove special character , white spaces from the col name

As you already know the schema hence create a YAML file and write the column name in YAML file. --define separator of read and write file, column name in YAML

Validate number of columns and column name of ingested file with YAML.

Write the file in pipe separated text file (|) in gz format.

Create a summary of the file:

Total number of rows,

total number of columns

file size

## Week 7-13 : Data Science Group Project :: Bank Marketing (Campaign)

### Data Set Link: https://archive.ics.uci.edu/dataset/222/bank+marketing

### Group Project Github Repo Link: https://github.com/cralph31/Data-Glacier-Final-Group-Project-Weeks-7-12-Deliverables.git

### Problem Statement:

ABC Bank wants to sell it's term deposit product to customers and before launching the product they want to develop a model which help them in understanding whether a particular customer will buy their product or not (based on customer's past interaction with bank or other Financial Institution).

### Why ML Model: 
Bank wants to use ML model to shortlist customer whose chances of buying the product is more so that their marketing channel (tele marketing, SMS/email marketing etc)  can focus only to those customers whose chances of buying the product is more.

This will save resource and their time ( which is directly involved in the cost ( resource billing)).

Develop model with Duration and without duration feature and report the performance of the model.

Duration feature is not recommended as this will be difficult to explain the result to business and also it will be difficult for business to campaign based on duration.

### Imbalance data set : 
If dataset is imbalance then try to use techniques to handle imbalance data set and report model performance of each imbalance technique used (avoid techniques which recommend not to utilize whole available data)

### Task:

Business Understanding

Data understanding

Exploratory data Analysis

Data Preparation

Model Building ( Logistic Regression, ensemble, Boosting etc)

Model Selection

Performance reporting

Deploy the model

Converting ML metrics into Business metric and explaining result to business

Prepare presentation for non technical persons.
 

### Data Set Information :

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y).

 

### Attribute Information:

Input variables:
#### bank client data:

1 - age (numeric)

2 - job : type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')

3 - marital : marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)

4 - education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')

5 - default: has credit in default? (categorical: 'no','yes','unknown')

6 - housing: has housing loan? (categorical: 'no','yes','unknown')

7 - loan: has personal loan? (categorical: 'no','yes','unknown')

#### related with the last contact of the current campaign:

8 - contact: contact communication type (categorical: 'cellular','telephone')

9 - month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')

10 - day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')

11 - duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.

#### other attributes:

12 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

13 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)

14 - previous: number of contacts performed before this campaign and for this client (numeric)

15 - poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')

#### social and economic context attributes

16 - emp.var.rate: employment variation rate - quarterly indicator (numeric)

17 - cons.price.idx: consumer price index - monthly indicator (numeric)

18 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)

19 - euribor3m: euribor 3 month rate - daily indicator (numeric)

20 - nr.employed: number of employees - quarterly indicator (numeric)

#### Output variable (desired target):

21 - y - has the client subscribed a term deposit? (binary: 'yes','no')

## Week 7: Deliverables

Submit a pdf document which should contain following details:

Team member's details : Group Name (give a name to your group), Name, Email, Country, College/Company, Specialization ( Data Science, NLP, Data Analyst)

Problem description

Business understanding

Project lifecycle along with deadline

Data Intake report

Github Repo link

## Week 8: Deliverables

Submit a pdf document which should contain following details:

Team member's details : Group Name (give a name to your group), Name, Email, Country, College/Company, Specialization ( Data Science, NLP, Data Analyst)

Problem description

Data understanding

What type of data you have got for analysis

What are the problems in the data ( number of NA values, outliers , skewed etc)

What approaches you are trying to apply on your data set to overcome problems like NA value, outlier etc and why?

Github Repo link

## Week 9: Deliverables

#### Data Cleansing and Transformation

Submit a pdf document and ipynb notebook which should contain following details:

Team member's details : Group Name (give a name to your group), Name, Email, Country, College/Company, Specialization ( Data Science, NLP, Data Analyst)

Problem description

Github Repo link

Data cleansing and transformation done on the data.

Try at least 2 techniques to clean the data ( for NA values : mean/median/mode/Model based approach to handle NA value/WOE and like this try different techniques to identify and handle outliers as well)

for NLP try different featurization technique and also clean the data using regex and python

Each member should code and review peers work. (Review comment should be present in the github repo)

Each team member should work on different data cleansing approach.

Note:

If one team member is using mean to impute values then other member should experiment on segmented approach or any other model based approach to impute the null values.

you are allowed to merge the code of each individual and work together to get good result.

Make sure code of each team member is placed at provided URL (single repository for whole team).

## Week 10: Deliverables

Submit a pdf document and EDA ipynb file which should contain following details:

Team member's details : Group Name (give a name to your group), Name, Email, Country, College/Company, Specialization ( Data Science, NLP, Data Analyst)

Problem description

Github Repo link

EDA performed on the data

Final Recommendation

## Week 11: EDA Presentation and proposed modeling technique

Team member's details : Group Name (give a name to your group), Name, Email, Country, College/Company, Specialization ( Data Science, NLP, Data Analyst)

Problem description

Github Repo link

EDA presentation for business users

Last slide of EDA should be dedicated to technical user which should contain recommended models for this data set.

## Week 12: Model Selection and Model Building/Dashboard

Select your base model and then explore 1 model of each family if its classification problem then 1 model for Linear models, 1- Model for Ensemble, 1-Model for boosting and other models if you have time (like stacking)

Please make sure selected model fits in your business requirement. For example : If your business does not want black box model then select only those models which can be used to explain the prediction.

As this is group assignment hence upload the code of each team member and other deliverables in the single repo and share the URL of that repo.

Interns of Data analysis Project should submit dashboard in this week. 

you are allowed to merge the code of each individual and work together to get good result.

## Final Project Report and Code

Provide the link of your code and report.

As it was group assignment hence go far a call with your team and discuss the solution of each member and

select that solution which is best and is per the requirement.

Power point presentation is must.

you are allowed to merge the code of each individual and work together to get good result. 
