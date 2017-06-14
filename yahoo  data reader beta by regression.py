Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from pandas_datareader import data as pdr
>>> import matplotlib.pyplot as plt
>>> import fix_yahoo_finance # must pip install first
>>> from scipy import stats
>>> import numpy as np
>>> data1 = pdr.get_data_yahoo('EFL.TO','2017-05-01','2017-06-14')[['Open','Adj Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/EFL.TO?period1=1493611200&period2=1497412800&interval=1d&events=history&crumb=GIjzhDQ8388
>>> data2 = pdr.get_data_yahoo('^GSPTSE','2017-05-01','2017-06-14')[['Open','Adj Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/^GSPTSE?period1=1493611200&period2=1497412800&interval=1d&events=history&crumb=GIjzhDQ8388
>>> a = data1['Adj Close'].pct_change()
>>> b = data2['Adj Close'].pct_change()
>>> a=a.dropna()
>>> b=b.dropna()
>>> slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
>>> slope
-0.0093767631720639184
>>> predict_b = intercept + slope * a
>>> pred_error = b - predict_b
>>> degrees_of_freedom = len(a) - 2
>>> residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
>>> plt.plot(a, b, 'o')
[<matplotlib.lines.Line2D object at 0x00000000036E3CF8>]
>>> plt.plot(a, predict_b, 'k-')
[<matplotlib.lines.Line2D object at 0x00000000084C2208>]
>>> plt.show()
