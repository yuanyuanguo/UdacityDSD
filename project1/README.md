# Project 1 - Blog Post :Exploring Stack Overflow Data 2017 


## CRISP-DM Framework

**Business Understanding**: 

We want to explore Stack Overflow 2017 data to better understand following business questions:

1. Description of the respondents, where they are and who they are?
2. What are the top known languages, top wanted languages among the professional developers and students?
3. Is the developer’s salary related to their country, language type, degree, working period?
4. A tempt of use linear regression and random forest to test whether StackOverFlow activity level could affect salary.

**Data Understanding** 

The dataset is about a survey provided by StackOverFlow in 2017, contains 2 files: A question list and related anwsers from developers. There are 51392 responders and each has answered 153 questions. We could see most of the responders are from English-speaking Contries like US, India, EU, etc..

**Data preparation** & **Data Modeling**: 

We needs to pick up relative data in purpose, so for each use case, we did data cleaning, NAN value dropout, biased data remving and relative column picking for data modelling to make sure our conclusion trustable and clear.

**Result Evaluation & Deployment**: 

Result and discussion are published in https://medium.com/@eros329/stackoverflow2017-schema-exploration-b6f935b7d3cd


## Result Evaluation & Deployment:

In this project we are trying to answer 4 business questions, and we have answers as following:
    
**1. Description of the respondents, where they are and who they are?**

A: The users are mainly English speaking code writers using StackOverFlow. They are mainly developers, students and non-developer code writers.

**2. What are the top known languages, top wanted languages among the professional developers and students?**

A: For developers and students, languages they use are different. Developers use JSP and SQL more, and students prefer Java and Python more.
  We could see python and swift is drawing more attention in future, and old school languages like C and matlab are about to go out-of-time.  

**3. Is the developers' salary related to their country, number of languages, degree, working period?**

A: The factor developers' salary should be a very complex question, here we just make simple test for simple purpose. 
  According to our test, working period and countries indeed are related to their salary. We could also see that people with college education (PhD, Master or Bachelor) are expected to achieve higher salaries, but also their is an abnormal data "primary school", which main caused by varies reasons for further studies. number of languages has no effect with salary.

**4. A tempt of use linear regression and random forest to test whether StackOverFlow activity level could affect salary.**

A: We try to use several method to predict salary by using activity related columns, but the result shows may salary are not affected by these factors.
But we should mentioned that, there are 153 questions in schema, which means if we could use all of this data for predict, the model could be powerful enough to find several methods to predict the salary by giving some of the factors. But we need to pick up good factors and ML models based on experience and analysis, and also need to be care of overfitting and data biasis. 
