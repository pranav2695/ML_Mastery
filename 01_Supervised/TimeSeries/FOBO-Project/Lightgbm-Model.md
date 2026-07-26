## Lightgbm with detrender and deseasonalizer
we use the class name called TargetTransformedSeries, which will have deseasonalizer, de trender and with lighgbm , with 12 previous lag as standard in parameter window = 12  
what is the cross validation ?
we want to have some confidence on the accuracies numbers we dont want to be lucky or unluck by chance so we divided the data into k folds then each time we will train are data on k-1 folds and 1 fold will be used as the test dataset, then we take the average accuracies metrics, which is a very reliable number   
for the time series as we cant shuffle the data we use the ExpandingwindowSplitter of sktime to keep on add the data after doing the testing on that data.  
Note: in the lightgbm regressor we use parameter strategy = recursive, so our model one predict one step at a time, after thatn we will give back this predicted step as a input and then it will again predict the next time. thats how it will predict the months in the forecast horizon.
NOTE: We also try to tune the window length based on teh training data length default values we give 12 lags but we are increasing those to 48 so that forecasting grid search cv can find the best number of lags based on time series.
## Vanilla model 
0. vanilla 0 model: 
    - Last 3 month amt values is less and equal to 0.1 
    - Last 3 months if no amt values is reported for the series 
    - Last 12 months amt values is less and equal to 1200
1. vanilla 1 model:
    - it return the series with mean as the values 
    - Any series having data points < 12  but not vanilla and any series (which was assigned vanilla in last execution) which has data points >= 12 but have at least one missing month
2. vanilla 2 model : 
    - will have data points greater than 12 and less 24 here we apply the growth rate 
3. vanilla 3 model :
    - will have data points greater than 24 and less than 36 here we apply the SES model
=======================================================
Here we create the model with deseasonlizer and detrender, we are using the sktime library here
  for TransformedTargetForecaster, it applies the transformation on the series  and it also 
  automatically bring back those changes when doing the prediction.
  also orders matters, during the .fit() they are applied top to botton and during .predict()
  they are applied bottom to top automatically.
  window length : previous lags to consider

## Outlier detection method 
1. First we are extended the data at starting and end by 6 data point so that we will be able to decompose the series better.
2. Now we will decompose the series using the seasonal decompose and use the residual to calculate the 3.5 IQR range to filter out the outliers 
3. There will be two conditions cond1 and cond2 for the less than 3.5 and greater than 3.5, using these conditions we  will filter out the amt column and subtract the resid from it  
And then remove the 6 from the front and back of the data which we added in the starting 

## Manual adjustment for outlier 

1. In the manual adjustment table we give the model type default , additive or multiplicative which we will be using in the seasonal decomposition 
2. For the manual adjustment we have option to add dates as the outlier by setting outlier col value as True and if we set as false then it will not be treated as the outlier 
4. Then we have constant we will multiple our outlier treated value by constant to have manual control on the values of the outlier treated value