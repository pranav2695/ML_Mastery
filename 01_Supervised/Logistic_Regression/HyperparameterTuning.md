## Hyper Parameters Tuning
Parameters are the internal variables of a model that are learned from the data during the training process. for eg linear regression we learn coefficients or weights and bias in deep learning.  
Hyper parameters are parameteres whose values are set before the learning process begins. These parameters are not learned from the data and must be predefined. They help in controlling the learning process and can significantly influence the performance of the models.
Hyper parameters is kind of meta parameter  which dont participate in the learning from data but structurally control it. thats why it is called hyper parameter.  
## Hyper parameters tunning techniques
1. GridSearchCV: it performs an exhaustive search over a specified grid of hyperparameters, using cross validation to determine which hyper parameters combination gives the best model performance.  
it will create the parameter space. it will give the best result as we try out all the combination.  
In the end you can create the pandas dataframe and analysis all the scores based on the mean scores that we are getting after cross validation.  
2. RandomizedSearchCV: If we dont have enough time, we will randomly try out the possibilities. we can give how many random possibilities. It is fast but we will get the sub optimal results.   
Technique that we to get the results fast and best we use bayesian optimization. we have some library like scikit opt, optuna and hyperoptuna
## Bayesian optimization 
In this we will first select the some random hyper parameters and analyze the result, we will have some data to guide us which direction we should go and then same thing we will do and reach the best hyper parameters.    
 