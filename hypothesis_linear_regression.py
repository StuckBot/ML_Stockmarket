# -*- coding: utf-8 -*-
"""Hypothesis_Linear_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vWj30FFyvDTTc5CSzKgSp7XcAy7thwc_

# **Hypothesis: Linear Regression**
"""

# Commented out IPython magic to ensure Python compatibility.
#import packages
import pandas as pd
import numpy as np

#to plot within notebook
import matplotlib.pyplot as plt
# %matplotlib inline

#setting figure size
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10
import pandas_datareader.data as web
import datetime

#for normalizing data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

# Define which online source to use
data_source = 'yahoo'

# define start and end dates
start_date = '2018-01-01'
end_date = '2019-12-31'
symbol = 'ICICIBANK.NS'
#symbol = 'GAIL.NS'
#symbol = 'ONGC.NS'
# Use pandas_datareader.data.DataReader to load the desired data list(companies_dict.values()) used for python 3 compatibility
web.DataReader(symbol, data_source, start_date, end_date).to_csv(symbol+'.csv')
df = pd.read_csv(symbol+'.csv')
df = pd.DataFrame(df,columns=['Date','Open','High','Low','Close']).round(decimals=2)
df.head()

#creating a separate dataset
disdata = pd.DataFrame(df,columns=['Date','Open','High','Low','Close'])

#setting index as date
disdata['Date'] = pd.to_datetime(disdata.Date,format='%Y-%m-%d')
disdata.index = disdata['Date']

#plot
plt.figure(figsize=(16,8))
plt.plot(disdata['Close'], label='Close Price history')

#creating a separate dataset
data = pd.DataFrame(df,columns=['Date','Open','High','Low','Close'])

from sklearn.model_selection import train_test_split
train, test = train_test_split(data, test_size=0.30,shuffle=False)
from sklearn.linear_model import LinearRegression

x_train = np.array(train.index).reshape(-1, 1)
y_train = train['Close']

# Create LinearRegression Object
model = LinearRegression()
# Fit linear model using the train data set
model.fit(x_train, y_train)

from sklearn import metrics

x_test = np.array(test.index).reshape(-1, 1)
y_test = test['Close']

x_train = np.array(train.index).reshape(-1, 1)
y_train = train['Close']

preds_train = model.predict(x_train)
print('\nError Report on TRAIN Data')
print('Mean Absolute Error:', metrics.mean_absolute_error(y_train, preds_train))  
print('Mean Squared Error:', metrics.mean_squared_error(y_train, preds_train))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train, preds_train)))

preds_test = model.predict(x_test)
print('\nError Report on TEST Data')
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, preds_test))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, preds_test))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, preds_test)))

#setting index as date
test['Date'] = pd.to_datetime(test.Date,format='%Y-%m-%d')
test.index = test['Date']

train['Date'] = pd.to_datetime(train.Date,format='%Y-%m-%d')
train.index = train['Date']

train['Predictions_train'] = 0
train['Predictions_train'] = preds_train

test['Predictions_test'] = 0
test['Predictions_test'] = preds_test

plt.plot(train['Close'])
plt.plot(test[['Close', 'Predictions_test']])
plt.plot(train[['Close', 'Predictions_train']])

"""RMSE = 25.5895 on TRAIN DATA
RMSE = 57.3500 on TEST DATA

RMSE = 8.4087 on TRAIN DATA
RMSE = 41.047 on TEST DATA

RMSE = 11.0870 on TRAIN DATA
RMSE = 46.6549 on TEST DATA

"""