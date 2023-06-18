# Project 4 - Data Scientist Capstone: Dog Breed Classifier 

""I found the readme given in the workspace here should be in another udacity CNN related case, so I still try to follow the Project Rubric of Data Scientist Project. So I did not upload a report.html in github, instead, I post the post in medium, You could found my post in :https://medium.com/@eros329/report-case-study-in-dog-breed-classifier-designing-udacity-data-scientist-capstone-project-5faf350c4759""

## Project Overview

Welcome to the Convolutional Neural Networks (CNN) project in the AI Nanodegree! In this project, you will learn how to build a pipeline that can be used within a web or mobile app to process real-world, user-supplied images.  Given an image of a dog, your algorithm will identify an estimate of the canine’s breed.  If supplied an image of a human, the code will identify the resembling dog breed.  

Along with exploring state-of-the-art CNN models for classification, you will make important design decisions about the user experience for your app.  Our goal is that by completing this lab, you understand the challenges involved in piecing together a series of models designed to perform various tasks in a data processing pipeline.  Each model has its strengths and weaknesses, and engineering a real-world application often involves solving many problems without a perfect answer.  Your imperfect solution will nonetheless create a fun user experience!

## Project Conclusion

In this project, I walked through how to build a Convolutional Neural Network (CNN) for image classification. In particular, the CNN developed for this project will attempt to predict the breed of a dog in a given photo. Just for fun, we’ll also determine which dog breed a human most resembles when provided an image of a person:)
To achieve such a function, in this project, we learn from the very beginning how to build up a CNN with Keras, to how to do transfer learning from more power pre-trained weights. The guide of this project provides quite a smooth learning curve for beginners like me. Many thanks! Udacity!

Here I will share some of my thoughts along with the key points I found in this project with you. And I wish it could somehow inspire people that have similar experiences:

    1. The first thing I’d wish to mention is the models and algorithms used in the project. According to the project’s guide, Haar Feature-Based cascade classifiers was used to detect if the image is a human face or not. This detector was tested on the first 100 images from the human and the dog datasets. It achieved 100% accuracy on the human images, but it also detected 11% of the dog images as human faces. And then, To detect dogs, a pre-trained ResNet50 model was trained and achieved 100% accuracy on the dog images, and it didn’t detect any dogs in the human face dataset. These 2 functions are combined together in the final step to judge the pictures’ content, which also usually happened in my normal job: Instead of developing a new algorithm with higher performance, sometimes combining multiple existing algorithms are more reliable way to reach the business requirement.
    2. The second inspiration is transfer learning from inception: I want to mention that detecting the dog’s breed is a challenging task. Even a human would have difficulty distinguishing between a Brittany and a Welsh Springer Spaniel. In the project, we have tried to build up the model from the very beginning, and we found the performance is quite bad, due to lack of training time and data. I have tried so many methods including modifying kernel size, conv2D filter, activation function, padding method, dropout method, BatchNormalization, and softmax. But the results are not accepted. But just by using inceptionV3 as the base of transfer learning, the accuracy has incredible improvement, even though in 2023 we had much better models like SAM or Blip2. This story prove the value and power of a pre-trained model again, which is the most important topic in AI-related development and research. As Sir Isaac Newton said: If I have seen further than others, it is by standing upon the shoulders of giants.
    3. At last, the third story I’d wish to share is I found that the quality of data is the key to the final function performance. Machine learning is like making a computer draw a very complex formula based on the data given. So what data you feed will affect what the resulting formula looks like. Even if you pick suitable architecture and algorithm trying to avoid overfitting and basis, data is always the most constrain of our daily development. For example, in the project, I found the final algorithm worked quite fine with pictures we found on the Internet. But If I change to a black-white photo or provide a picture with more than 2 entities, the algorithm was doomed, such a story also happened in my daily work. Because it is hard for us to develop a function that can handle all new scenarios, it is important to have a very clear and overall business requirement analysis at the beginning of the project and use the analysis result to carefully gather enough clear data for training. Engineers often take this process lightly, leading to incomplete data collection and eventually impacting final function performance.
Here is my lesson learning in the Capstone project, And hops my experience could help you with your daily work!

Cya:)

## Evaluation

Your project will be reviewed by a Udacity reviewer against the CNN project [rubric](https://review.udacity.com/#!/rubrics/810/view).  Review this rubric thoroughly, and self-evaluate your project before submission.  All criteria found in the rubric must meet specifications for you to pass.

## Project Submission

When you are ready to submit your project, collect the following files and compress them into a single archive for upload:
- The `dog_app.ipynb` file with fully functional code, all code cells executed and displaying output, and all questions answered.
- An HTML or PDF export of the project notebook with the name `report.html` or `report.pdf`.
- Any additional images used for the project that were not supplied to you for the project. __Please do not include the project data sets in the `dogImages/` or `lfw/` folders.  Likewise, please do not include the `bottleneck_features/` folder.__

Alternatively, your submission could consist of the GitHub link to your repository.
