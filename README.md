## Presidential Tweets Sentiment Analysis

### Introduction

In this project, we are given an excel file containing tens of thousands of tweets (data) about Obama and Romney during the presidential election of 2012 along with the “opinion” (label) of these tweets. The opinions are categorized into 4 classes, -1 negative opinion, 0 neutral or no opinion, 1 positive opinion and 2 mixed opinion. Our objective is to utilize supervised learning techniques to build a classifier to classify tweets into three classes: -1 negative opinion, 0 neutral or no opinion and 1 positive opinion. In other words, given N training samples {(x1, y1), …, (xN, yN)}, where xn is training data and yn is its associated label (n∈1,…, N), the label Yt = {yt1,…,ytM} of testing data Xt = {xt1,…,xtM} of size M should be predicted. The training data set and label set are denoted by X = {x1, …, xN} and Y = {y1, …, yn}.

The evaluation of the classifier contains 2 parts. The first part is 10 fold cross-validation, where the given datasets are divided randomly into two group, training and testing.  And the second part is demo, where the classifiers are tested using unseen data and all the given data can be used for training.


### Running the tests
SImplily run the TweetClassifier.py file in the src directory.
