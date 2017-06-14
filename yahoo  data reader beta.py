Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> from pandas_datareader import data as pdr
>>> import fix_yahoo_finance # must pip install first
>>> data1 = pdr.get_data_yahoo('EFL.TO','2017-05-01','2017-06-02')[['Open','Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/EFL.TO?period1=1493611200&period2=1496376000&interval=1d&events=history&crumb=vcz5.EdLXnK
>>> data2 = pdr.get_data_yahoo('^GSPTSE','2017-05-01','2017-06-02')[['Open','Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/^GSPTSE?period1=1493611200&period2=1496376000&interval=1d&events=history&crumb=vcz5.EdLXnK
>>> data2
 
>>> import matplotlib.pyplot as plt
>>> plt.show()
>>> data['Return_Out'] = data['Close'].pct_change()
>>> data['Return_Out']
 
Name: Return_Out, dtype: float64
>>> data['Return_Out'].plot()
<matplotlib.axes._subplots.AxesSubplot object at 0x0000000009556320>
>>> plt.show()

>>> a = data1['Close'].pct_change()
>>> b = data2['Close'].pct_change()
>>> a=a[~numpy.isnan(a)]
>>> b=b[~numpy.isnan(b)]

>>> import numpy
>>> covariance = numpy.cov(a,b)[0][1]
>>> variance = numpy.var(b)
>>> beta = covariance / variance

>>> print ("The beta for your stock is " + str(beta))
The beta for your stock is 0.000973391854145
>>> 
