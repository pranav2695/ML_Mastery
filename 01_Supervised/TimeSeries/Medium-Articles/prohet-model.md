## Facebook Prohet 
Input to model is two columns ds and y. ds is datestamp column should be of a format expected by Pandas, ideally YYYY-MM-DD. Y column must be numeric and represent the measurement we wish to forecast.
we plot the forecast with prophet.plot(), prophet.plot_components, with the component plot we can see the trend yearly, seasonality and weekly seasonality of the time series.
use the code m.plot_componenet(forecast)  
## Saturating Forecast  
Prophet uses a linear model for its forecast. when forecasting growth, there is usually some maximum achievable point: total market size, total population size, etc. This is called carrying capacity and the forecast should saturate at this point.  
this information we can add in the seperate column called 'cap'. this we need to add for each row, if the market cap is growing we add the growing value for the cap.  
then we fit the model as before, except pass in an additional agrument to specify logistic growth.  
m = Prophet(growth='logistic')  
m.fit(df)
### Python
future = m.make_future_dataframe(periods=1826)  
future['cap'] = 8.5  
fcst = m.predict(future)  
fig = m.plot(fcst)  
prohet saturate at 0 in the minimum side but we can also change that if required.  
### Saturating minimum 
Here we add the column floor in the same way as the cap column specifies the maximum  
## Trend changePoints  
In the real life time series, trend of the series can change frequently and prohet automatically try to detect those trends and adjust the forecast, if you want the fine control the points where trend is changing we can use the trend change points.  
The number of potential changepoints can be set using the arguments n_changepoints, but this is better tuned by adjusting the regularization. 
# Pythonv (to plot the changepoints)
from prophet.plot import add_changepoints_to_plot  
fig = m.plot(forecast)  
a = add_changepoints_to_plot(fig.gca(), m, forecast)  
By default only 80 percent of time series will be market with change points but we can also change this by adjusted changepoint_range = 0.9 , this will have 90 percent of data.  
## Adjusting trend flexibility
if the trend changes are being overfit (too much flexibilty) or underfit (not enough flexibilty), you can adjust the strenght of the sparse prior using the input argument changepoint_prior_scale.   
Decreasing it will make the trend less flexible  
## Specifying the locations of the changepoints  
we can manually add the data points for trend change point rather than automatically detecting it.  
# Python  
m = Prophet(changepoints=['2014-01-01'])  
forecast = m.fit(df).predict(future)  
fig = m.plot(forecast)  
# Seasonality, Holiday Effects, And Regressors  
we will have column holidays and ds and a row for each occurance of the holiday. it must include all occurance of the holiday, both in the past(back as far as the historical data go) and in the future (out as far as the forecast is being made).  
we can also include the lower window and upper window as a columns