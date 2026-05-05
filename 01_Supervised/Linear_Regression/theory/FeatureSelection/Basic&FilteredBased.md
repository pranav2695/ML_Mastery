# Feature Selection 
Features are basically independent variables.  
why we do the feature selection, first curse of dimensionality (with certain number of features you will get the best results) Mostly because of sparsity. second computational complexity. Third is interpretabilty (basically inference), if we have more numbers of columns then it becomes difficult to do the inference.  
## Types of Feature selection 
1. Filtered based techniques: In this method we use statistical measure to score each feature independently and then select a subset of feature based on these scores.we will focus one feature at a time. if we have any duplicate feature then we can drop it one feature
    - variance thershold: it will applied on constant (variance is zero) so we can drop these columns and quasi constant feature, variance is very close to close and feature is quasi constant feature. we define the thershold of variance and then we check if the variance value is less than that thershold we drop the column. in the sklearn.feature_selection VarianceThreshold. normalise or std the data 0.1 to 0.01 is the good thershold value  
        - Ignores the target variables   
        - Ignores the feature interaction  
        - sensitive to data scaling  
        - Arbitary Threshold Value  

    - Correlaton: Pearson correlaton coefficient (-1 to 1) we tried to reduce the multicollinearity and automatically we reduce the features.  
        - Linearity Assumption 
        - Doesnt capture complex relationship 
        - Threshold Determination 
        - sensitive to outliers
    - Annova: we use when we have input is numerical and output is catergorical (1 way annova) with categorical value > 2, we calculate the f statistics MS Between / MS within  
        - Disadvantages
            - Assumption of normarlity 
            - Assumption of homogeneity of variance
            - independence of observation 
            - Effect of outliers 
            - Doesnt account for outliers 
    - chisquare: it is used for the both catergorical values features and target variables. We create the contingency table basically frequency table, we call it observed values, we make one more table, this is called expected value we will sum the marginal sum and divided by grand total of the table. i have ideal data and observed the data, here null hypothesis is there is not relationship. calculate the chi square statistic. Inside scipy stats we have chi2_contingency. lesser the p value more the important feature 
        - Disadvantages
            - Categorical data only
            - Independence of observations
            - sufficient sample size 
            - No varaible interaction 
    - Mutual info:
2. wrapper method 
3. Embedded techniques
4. Hybrid techniques
## Mutual Information 
It is the measure of the dependency between two variables. It quantifies the amount of information obtained about one random variable through observing the other random variable. It is the fundamental quantity in information theory  
$MI = \sum_{x=X}\sum_{y=Y}p(x,y)\log[p(x,y)/p(x)p(y)]$    

p(x,y)---> joint probability   
p(x), p(y) ---> marginal probability
- we will create the contingency table and for each value in the table we will calculate using above formula 
- it can capture linear and non linear data both 
- it will also work on the numrical data also, it will create the histogram 
- we have function called mutual_info_classif, this is for categorical data. for regression we have mutual_info_regression. 
- we can use with the selectkbest   
## Disadvantages 
- Estimation difficulty 
- Assumes Large sample sizes
- Computionally Intensive  
- Difficulty with continous variables 
- No Direct indication of the nature of relationship 
- Doesnt account for redundancy 