## Lasso regularization 
$L = MSE + \lambda |W|$  
if increase the values of lambda then it will lead to underfitting, values of lambda between 0 to 1, In Lass reg. coefficients will become zero.  
we can use this as a feature selection.  
Affect on the loss fucntion is , loss fucntion move to exact zero position and shape will also shape.  
## why Lasso regularization create the sparsity (some values becomes zero)  
Because in  numerator we have - $\lambda$ and due to this it will make the m = 0 and as m starts to make the negative formula will change to use the one with + $\lambda$. then algo stops that the zero value.  
## Elastic net regularization   
It is the combination of both lasso and ridge. lambda = a + b and L1 ration = a/(a+b). 
using these can choose which one we want to apply more which type of regularization.  
If the data contains multicollinearity we use the elastic net regularization. 
we have twoo in the sci ket learn to use the regularization one is direct class elastic net and other is SGD regressor. 
 
