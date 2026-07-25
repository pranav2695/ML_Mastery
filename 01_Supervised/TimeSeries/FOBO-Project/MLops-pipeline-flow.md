## Learnings 
we are doing the forecast at monthly level and grain is Country and Subbrand, generating the forecast for 18 months 
they sell the concentrate to bottler who further add sugar, Gas, water package the product and then sell to end customer.
full profit loss was the scope 
1. volumes 
2. COGS
3. Gross sales 
4. OPEX-A&M, G&A, Fixed S&D.
##  Steps in the Pipeline 
1. prepare the model ready data for training by adding the external indicators data like food inflation, unemployement, GDP growth rate, Holidays in the single data with the column metric, which helps to identify the weather it is sellout or other indicators. 
2. Assign the default model to a new time series comes in the latest data, if the time series meeting certain condition like data points more 12 , certain value in the forecast column for eg amt column, then we assign the machine learning model. Other wise we assign the vanilla models. 
3. Now we these model we generate the past 12 months forecast, as this forecast is required in teh model competition notebook to consider which is the best moel for this production run. 
4. For the current execution we will do the production run and generate the forecast for all the machine learning models present for the particular serie. 
5. Same we will do the statistical models also 
6. Now for the current execution we will select the best model based on the historical 12 executions. 
7. After this we will consolidate the machine learning models and statistical models together. 

## Post processing pipelien 
- Here we will stitch the Actuals, Manuals and outlier treated actuals in the same tables, then we have few more notebook to send the data to 1. tableau dashboard to analyze the forecast and consume by business 2. we also the data to IBM tm1 planning tool where financial planner use our AI forecast as the base to do the planning and projections 

### Question 
1. why did we go with the lightgbm models ?
Ans. we did the experiments with all the modela and we narrow down it two model which is facebook prophet and lightgbm. we went ahead lightgbm because we were using the microsoft stack and model is also maitain by them so support will be good and accuracies were good. 
