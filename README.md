# Time series modeling

# Presiqutes

* Python 3.8+
* Pip 

It recomends to create a virtual environment to run the notebook

```shell
python -m venv .venv
source .venv/bin/activate
```

# Data


# Models
The models in demostration are:
* ARIMA
* prophet
* xgboost
* lstm

### ARIMA (AutoRegressive Integrated Moving Average)

ARIMA is a widely used time series forecasting method. It stands for AutoRegressive Integrated Moving Average. ARIMA models capture time-dependent patterns and trends in data. It has three key components:

- AutoRegressive (AR): This accounts for the linear relationship between the current observation and previous observations, indicating how past values influence future values.
- Integrated (I): The 'I' denotes differencing to make the time series stationary, which helps remove trends and seasonality.
- Moving Average (MA): This accounts for the relationship between the current observation and a weighted average of past prediction errors.

ARIMA models are effective for capturing **linear relationships** and are suitable for data with known temporal structures.

### Prophet

Prophet is a forecasting model developed by Facebook. It is designed to handle time series data that may have missing values, outliers, and irregular patterns. Prophet decomposes time series data into three components: **trend**, **seasonality**, and **holidays**. It uses a customizable additive model to capture these components and provides a reliable way to forecast time series data, even when the patterns are complex or unpredictable.

Prophet is user-friendly and requires minimal parameter tuning, making it a popular choice for business and financial time series forecasting.

### XGBoost

XGBoost is a machine learning algorithm that can be applied to time series forecasting by treating it as a supervised learning problem. It is a gradient boosting algorithm that builds an ensemble of decision trees. To use XGBoost for time series forecasting, you need to **transform your time series data into a supervised learning format**, considering time lags as features.

XGBoost is known for its flexibility and high performance. It can capture complex patterns and relationships in time series data and is often used when more advanced models are needed.

### LSTM (Long Short-Term Memory)

LSTM is a type of recurrent neural network (RNN) that excels at handling sequential data, making it suitable for time series prediction. LSTMs can capture long-term dependencies and learn intricate temporal patterns within the data.

LSTMs consist of memory cells, which can store information over long sequences, and gates that control the flow of information. These features make LSTMs particularly effective for time series forecasting, especially when dealing with complex and non-linear relationships in the data.

LSTMs require more data and parameter tuning compared to the previous models but can provide powerful results for challenging time series forecasting tasks.


# Caveats and Remarks






