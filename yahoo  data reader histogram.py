Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from scipy.stats import norm
>>> from pandas_datareader import data as pdr
>>> import fix_yahoo_finance # must pip install first
>>> import matplotlib.pyplot as plt
>>> data = pdr.get_data_yahoo('EFL.TO','2017-05-01','2017-06-02')[['Open','Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/EFL.TO?period1=1493611200&period2=1496376000&interval=1d&events=history&crumb=CY\u002FU5n0pfgE
b'Skipping line 4: expected 1 fields, saw 2\n'

>>> data['Return_Out'] = data['Close'].pct_change()
>>> k=data['Return_Out']
>>> k.hist()
<matplotlib.axes._subplots.AxesSubplot object at 0x0000000008AE1828>
>>> plt.show()
>>> plt.show()
>>> k.hist()
<matplotlib.axes._subplots.AxesSubplot object at 0x0000000008B3CEB8>
>>> plt.show()
