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
