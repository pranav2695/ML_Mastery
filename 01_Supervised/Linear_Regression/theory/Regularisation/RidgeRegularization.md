# Ridge Regularization (L2)
It is the regularization technique where we add the regularized terms $\lambda (\beta_1^2 +\beta_2^2 + .... )$  
Beta are the coefficients of linear regression coefficeints
- for the maths result, In the end formula to calculate the m will have lambda in the denominator, due to this when we increase the lambda it will decrease the value of m or beta (coefficients)
- As it is the regularisation technique it can be solved by using OLS and Gradient descant. 
## Ridge Regression using Gradient Descent
$L = (XW-Y)^T(XW-Y) + \lambda w^Tw$  
Using above loss function we can find the derivatives and then using gradient descant we can keep on update the weights and bias term till specified iteration.   
## 5 Key points of ridge regularization
1. How the coefficients get affected: As the value of the lambda is increase, coefficients will start decrease toward 0 but will not become zero.  
2. High values are impacted more: if the coefficient is higher then it will decrease more faster.  
3. Bias Variance Tradeoff : if lambda we increase, Bias will high and variance will decrease  
4. Impact of Loss fucntion : if we increase the lambda the loss function also starts moving to zero.  
5. why called Ridge : Hard constraint ridge contrain   
- Only use ridge regression when you have more than 2 columns.
 
