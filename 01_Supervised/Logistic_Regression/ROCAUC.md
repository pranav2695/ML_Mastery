## why ROC-AUC curve
It is used for the classification problems, to help select the threshold. for eg in the email spam classifier we dont want any important mail to go in spam so 0.5 probability is not the best one, we can increase this to be more sure that mail is spam.  
ROC-AUC curve helps us to find this threshold.  
## True positive Rate-->Benefit
$TPR = TP/(TP + FN)$  
We want to maximize this, basically TP we want to improve,   
## False Positive Rate--> Cost
$FPR = FP/(FP + TN)$  
## ROC - AUC curve  
it is the graph between the TPR vs FPR.  
How to draw this, we first  select one threshold and calculate the TPR and FPR, plot it.  
In way we can say it is the plot between benefit vs cost.  
- We have low threshold then TPR and FPR both will increase.  
- if we have high threshold then TPR and FPR both will decrease.  
- Best threshold is farthest from the linear line or closest to TPR values one. 
## Area Under curve  
The AUC - roc curve is used to compare the different models.   
- if AUC is 1 indicates that the model has perfect discrimination, it correctly classify all positives and negatives instances.  
- AUC is 0.5 , it is like the random guessing
- AUC is 0, then it is the worst model.