# Wrapper Methods
In the filtered based we only study relationship of one feature at a time with the target variables. for eg latitude may not have good relationship with target variables but latitude and longitude both will have good relationship with the target variable.  
This method involves using a predictive model to score the combination of features. they are called wrapper method because they wrap this type of model based evaluation aound the feature selection process.   
we generate the subsets of features with target variable and then apply the linear regression and calculate the r2 and subset which have highest r2, we will select that subset of features
## Types of wrapper methods
1. Exhaustive feature selection 
2. Forward feature selection 
3. Backward elimination 
4. Recursive feature elimination 
## Exhaustive feature selection  
Here we will create the subsets and apply the models and then select the subset on which error minmum or r2 is highest.   
## Disadvantages 
    - Computational complexity: Models we will train if we have n features is $2^n -1 $
    - Risk of overfitting
    - To select the good evaluation metric
Note we have use MLXtend lib 
## Sequential Backward selection / Elimination
In the technique we remove one feature and train the model and calcualte the scores, we select the best result and then again we will remove the one feature and create the model, calculate the scores. select the best score model. Number of iteration is equal to number of features. now we will take best of each iteration and select the best of all the iteration
## Advantages 
1. Faster: number of models we create here is $n(n+1)$  
Note Inside the MLexnt we have SFS(lr, k_features='best', forward=False, floating=False, scoring='r2', cv=5)
we have plot also plot sequentail Backward elimination
## Disadvantages
1. we are doing the local selection. 

## Sequential Forward selection 
In this we will add the feature one by one and calcualte the scores, first we will add one column and calculate the scores, then again and one more column and so on. after this we pick best model in each iteration and then pick best of these.  
Note: Based on the number features we want to keep we can use the forward or backward technique. if we want to keep more features then we can do the backward elimination and if we want to keep less number of features then we can use the forward selection.  
Note: we can provide the tolerance in the sklearn, 
## Advantages 
1. Better accuracy 
2. Interaction of features
## Disadvantages 
1. Computational complexity 
2. risk of overfitting 
3. Model specific

