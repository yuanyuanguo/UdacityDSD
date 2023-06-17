#Project 3 - Recommendation Engines IBM

## Introduction
In this project, we'll develop different recommendation engines to provide users with different articles they may have an interest in. 
## Analysis and development process
The following steps were followed throughout the development of the project:
  ### I. Exploratory Data Analysis
  In order to have a better overview of the data, we did a data exploratory analysis.
  ### II. Rank-Based Recommendations
   A recommendation engine based entirely on the popularity of the articles available on the IBM platform is developed to provide users recommendations on new articles.
   ### III. User-User Based Collaborative Filtering
   In this section, two different versions of collaborative filtering recommendation engines are developed. They try to identify similar users among the datasets to recommend users new articles that they have not yet interacted with.
   ### IV. Content-based recommendation
   This section is not required, so sorry due to time limitation, I will learn by my-self later on.
   ### V. Matrix Factorization.
   Finally, a machine learning approach should be utilized to build recommendations. Using the user-item interactions, we need to build out a matrix decomposition. Using the decomposition, we need get an idea of how well the predictions are.
 
 ## Conclusions
 
We observe that we have an increasing training accuracy until around 300 latent features and then the increase is marginal. At the same time, the testing accuracy remains above 0.93 while increasing the latent features. The F1_score is a better indicator and in this case, the training F1_score also drastically reduces to increase around 300 latent features. The F1_score on the other hand remains very low with a maximum of 0.131 at 90 latent features.

The main problem with this method for this dataset is that we have a very low number of users (20) for which we can make predictions. A larger dataset should enable to improvement the results. and also the classes are very unbalanced and the accuracy poorly represents the ability to correctly predict if the user saw a movie or not.

For me, as I discussed in the project, I will try to use some reinforcement learning algorithms or other ML methods to have a try. Users' behavior and taste could change over time, and the lack of historical data is a problem that we always faced to. So perhaps if we model such a system as a game of searching and apply even a multi-bandit or e-greedy algorithm, the result could be improved.
