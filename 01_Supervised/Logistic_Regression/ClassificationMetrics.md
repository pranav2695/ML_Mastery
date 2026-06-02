## Accuracy
It is the ratio of number of correct prediction to Total number of prediction.    
In the multiclass problem also it will remain same we only need to check the correct prediction and divide them by Total number of prediction.    
Accuracy score depends on model and problem statement.  
## Confusion metrics
accuracy = TP + TN/ (TP+TN+FN+FP)  
- False positive (Type 1 error)  
- False Negative (Type 2 error)    
In the Imbalance data accuracy gives very bad results, we should use precision or recall in these cases.  
## Precision  
where we want less False positive,    
Precision = TP/(TP+FP)  
## Recall  
In these case False Negatives are important
 Recall = (TP/(TP+FN))  
## F-1 Score 
Where we are not sure weather precision is more important than recall or vice versa.  
$F1 Score = 2PR/(P+R)$  
F1 score always at the lower side of precision or recall.
## Calculation of Precision and recall for the multi class 
So here we first calculate the precision and recall of the individual calls you the above formulas and then we have two option to calculate the single value of precision or recall 
- weighted: where we give the class weightage to the precision or recall 
- Macro: Here we dont have any weights same weight given to each class for precision or recal.  

