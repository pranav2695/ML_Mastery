# Embededd Methods 
Embedded methods used to remove the disadvantages of wrapper and filter based method, we do consider the feature interaction and they are fast. Feature selection will become the part of the model building. Feature selection is part of model construction process. In the machine learning algo have coef_ or feature_importance_ attributes, can be used for feature selection. regression , regularization and tree based models have these attributes  
## Linear Regression 
- $\beta$ they are actually feature importance, make sure all the 5 assumptions should be true.
## Regularised Model
- these includes a penalty term in the loss function during training. The penalty term discourage the learning of a too complex model, which can help prevent overfitting.
- Lasso, Ridge, ElasticNet
## Decision tree
- we have attribute feature_importance and with the help of this we can select the features. 
Note : In the scikit learn we have different class SelectModel which we can use for the feature selection sklearn.feature_selection import SelectFromModel  (we have parameter thereshold values mean it will calculate all the values of all the features and select the features who values is greater than mean )  
## Advantages 
- Performance 
- Efficiency 
- Less prone to overfitting: Tune the hyper parameters
## Disadvantages 
- Model specific
- complexity 
- Tuning required 
- Stability 
