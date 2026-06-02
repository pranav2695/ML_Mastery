## Cross validation 
we use hold out approach, train-test-split  
## Problem with hold out approach
- variability: Accuracy will depend on the training data, there is high variance in the accuracy if training data changes.  
- Data inefficiency: it uses a portion of the data for training and different portion for testing.  
- Bias in performance estimation: if the data is less then bais will increase
- Less reliable for hyperparameter tuning: there is a risk of overfitting to the test set because information might leak from the test set into the model.  
## why is hold out approach used then
- simplicity
- computational efficiency 
- Large datasets  
## Cross validation 
It comes under the concept of resampling, it has two ways one is cross validation and bootstrapping.  
so cross validation is a resampling technique, cv have two main CV 
1. Leave one out cv: if we have n row then it will form n models, one row will become test set and n-1 will become the training set. same we will repeat. we will calculate the average of all the n models. for scikit learn we have cross_val_score. also we cant cal the r2 sq for 1 row. so we can take all the models and take the average.

Advantages  
- use of data, less bias, No randomness

Disadvantages  
- Computational expensive, High variance, inappropiate performance metric, Not ideal for imbalanced data.  

2. Leave p out cv: In place of one out we keep the p data points in test set.
for k fold
1. k-fold
In the k fold technique we divide the training set into k folds and use we use k-1 fold for training and 1 for testing and repeat k times with different training and test set. it is generally k = 5 or 10. then we use the one model, model is same.  
Note: Cross validation is for model evaluation not for model selection.   
Advantages  
- Reduction of variance, Computationally inexpensive  
Disadvantages  
- Potential for High bias, May not work well with imbalanced classes.
2. stratified CV  
In this porpotion of classes will be same, and then we can take the average. we can use stratifiedkfold object.
3. Nested cv
## Data leakage
where information from outside the training data set is used to create the model.  
## ways in which data leakage  
1. Target leakage: when your predictors include data that will not be available at time you make prediction. for eg reversed transaction column, like kind of refund and in future this information wont be present.  
2. Multicollinearity
3. Duplicated data
4. Preprocessing data leakage: Missing data, same scale, transformation. it can also happen in train test contamination or improper cross validation
5. Hyperparameter tunning: If we are tuning the model so we ask the test data weather the results are good or not then making adjustments accordingly in the models.   
## Ways in which Data Leakage
1. Review your features: Any column wont be available during the prediction
2. unexpectedly high performance
3. Inconsistent performance between training and unseen data
4. Model Interpretability: like feature importance
## How to remove the data leakage  
1. Understand the data and task
2. careful feature selection 
3. Proper data splitting
4. Pre processing inside the cross validation loop
5. avoid overlapping data  
In the cross validation also we should use the pipeline and after the fold creation we should not use the test fold info for the   
we divide the data in 3 parts train, test and validation. 