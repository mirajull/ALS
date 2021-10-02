# ALS
CSE472 (Machine Learning Sessional) Assignment 3: Matrix Factorization for Recommender System


# Introduction

In this assignment, you’ll be building a recommendation system to make predictions. You’ll be
given data that comprises Users, Items, and Ratings. We’ll focus on the User-Item utility matrix
and build an alternating least square (ALS) based recommendation systems.

# Dataset

You are given a comma separated file titled “data.csv" to be used as the dataset for this assignment.
The file contains 24983 rows and 101 columns. First column indicates the number of rated products
by the user corresponding to row. Next 100 columns indicate the rating given by the user of that
row for 100 items. A 99 indicates no rating.

Use the following guidelines.

1. Taking ratings data from the given data set, build an ALS model with a small number of
latent factors, between 10-50 factors.
2. We strongly recommend that you first try your code on a smaller dataset.
3. Split the data set into 60-20-20 train-validate-test partitions. That is, the first 60% of the
data is the training set. The next 20% is for validation and the remaining 20% is for test.
You’ll use the training set to learn your ALS model and use the validation set to choose
the regularization parameter and the number of latent factors. Your splits will randomly
select ratings so that every portion of your matrix is sampled uniformly.
4. You’ll evaluate these systems via RMSE (root mean square error) metrics on Validation
and Test sets. Make sure you try different regularization parameters 𝜆 ∈
(0.01, 0.1, 1.0, 10.0) and several latent factor dimensions 𝐾 ∈ (5, 10, 20, 40) and select
the model that gives you the best RMSE on the validation set.
5. Once you have finished choosing your model using the validation set, write a simple
recommendation engine that will take the ALS model and test it on the test set and report
that error as your final error metric.
6. You can use any data structure library for sparse matrix representation and any linear
algebra library for matrix inversion.

![image](https://user-images.githubusercontent.com/18558507/135729552-212ae842-14c0-41d8-a6a7-b6e998b5c0d4.png)





