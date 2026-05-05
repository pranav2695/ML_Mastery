# Bias variatioin tradeoff
## The Hidden truth 
- Biggest problem in the machine learning is that, by using the sample data we need to make the model to predict the population data.
we have relationship between reducible error, Bias and variance  
$reducible error = Bias^2 + variation$  
Bias variance decomposition 
## Bias variance Trade off
Bias: The inability of a ML model to fit the training data, if the model is bad it means it has high bias model.  
Variance: how much the prediction of the ML model change by changing the Training data,  
when we will have high bias then low variation and vice versa, we have trade off between those.   
## Expected value and variance 
It represents the average outcome of a random variable over a large number of trails of experiments. when we calculate the mean in a way we are calculating the expected value, it is roughtly equal to population mean     
$E[x] = \sum x_i P(x_i)$  
$E[x] = \int x_if(x_i)dx$  
$var(x) = E[x^2] - (E[x])^2$  
above formula is the variation in bias variation trade off  
## What exactly are Bias and variance Mathmematically 
$Bias = E[f^{'}(x)] - f(x)$   
In the context of machine learning and statistics, bias refers to the systematic error that a model introduces because it cannot capture the true relationship in the data. It represents the difference between the expected prediction of our model and the correct value which we are trying to predict. More bias leads to underfitting, where the model does not fit the training data well.
## variance
$var(f^{'}(x)) = E[(f^{'}(x) - E[f^{'}(x)])^2]$
## Bias variance decomposition 
Bias variance decomposition is a way of analysing a learning algos expected generalization error with respect to a particular problem by expressing it as the sum of three very different quantities: bias, variance and irreducible error. 
$MSE = reducible-error + irreducible-error$  
$reducible error = Bias + variance$  
$loss = (Bias)^2 + variance + some error$  
Linear regression is high bias low variance model 
Decision Tree is low bias and high variance model


