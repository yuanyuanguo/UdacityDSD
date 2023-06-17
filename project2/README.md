# Project 2 - Disaster Response Pipeline Project
As what happened in Project 1, I also faced internet problems via VPN in China. I was trying to upload the 2 original .csv files(just 10Mb) but failed so many times..
So perhaps I may ask the supervisor to see into my workspace in Udacity if they want to run the whole project from the beginning.
But if you just want to test the function of the .pkl file, I managed to upload it..(even though I do not know why it succeeded..)
I also attached several screenshots of evidence.

## Project Description:
The main purpose of this project is to build a model to classify disaster messages and enable users to check the category of a new input via a given web app. The data is given by 2 .csv files including 2 types of languages. 

## Related Works:
1. Firstly I fill in the given guide **ETL Pipeline Preparation_YG.ipynb** and **ML Pipeline Preparation_YG.ipynb**.
  in **ETL Pipeline Preparation_YG.ipynb**, I merged the 2 .csv files, split categories and did necessary data cleaning
  in **ML Pipeline Preparation_YG.ipynb**, I tried several algorithms given by sklearn for the given requirement.
    first is random-forest with TDF-df features, and then tried grid-search, and then I tried RidgeClassifierCV as a classifier and achieve the best result among the tests.
2. And then, based on the guides, I filled the **process_data.py** and **train_classifier.py**.
   in **process_data.py**, for I am not familiar with file_paths, I faced many problems, but after a huge number of tests, I manage to figure it out.
   in **train_classifier.py**, due to RidgeCV acting best in the guide step, so I picked RidgeCV in the model creating function.

3. And then, modify model and data path in **run.py** and the website magically works
  to write everything in function mode also consume several time, and I did not change the initial DB name and model name to my own..
  So the DB name and pkl name as the command given in Instructions: 'data/DisasterResponse.db' and 'models/classifier.pkl'
5. After testing, the website works fine with both English and the original language,

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

