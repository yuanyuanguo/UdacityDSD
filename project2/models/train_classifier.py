import sys
# import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import re
import sqlite3

import sqlalchemy
from sqlalchemy import create_engine

from sklearn import multioutput
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import SGDClassifier, RidgeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, fbeta_score, make_scorer, confusion_matrix

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download(['punkt', 'wordnet', 'stopwords'])


def load_data(database_filepath):
    # load data from database 
    cstr="sqlite:///"+database_filepath
    cstr
    engine = create_engine(cstr)
    
    df = pd.read_sql_table("disaster_response_messages", con=engine)
    X = df['message']
    Y = df.iloc[:, 4:]
    category_names = Y.columns
    return X,Y,category_names 

def tokenize(text):
    # normalize text
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    # extract the word tokens
    tokens = nltk.word_tokenize(text)
    # Lemmanitizer
    lemmatizer = nltk.WordNetLemmatizer()
    # List of clean tokens
    token_lemmed = [lemmatizer.lemmatize(w).lower().strip() for w in tokens]
    return token_lemmed

def build_model():
    # try applying RidgeClassifierCV as classifier
    new_pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', multioutput.MultiOutputClassifier (RidgeClassifier()))
        ])
    #new_pipeline.fit(X_train, y_train)
    return new_pipeline

def evaluate_model(model, X_test, Y_test, category_names):
    y_pred_ridgeCV = model.predict (X_test)
    accuracy = (y_pred_ridgeCV == Y_test).mean()
    accuracy

def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()