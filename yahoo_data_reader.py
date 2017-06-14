Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas_datareader.data as pdweb
>>> from pandas_datareader import data as pdr
>>> import fix_yahoo_finance # must pip install first
>>> data = pdr.get_data_yahoo('EFL.TO','2017-05-01','2017-06-02')[['Open','Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/SPY?period1=1493611200&period2=1495512000&interval=1d&events=history&crumb=dqlOsu.NuMJ
>>> data.plot(figsize=(10,10), 1w=2)
SyntaxError: invalid syntax
>>> data
                  Open       Close        High         Low     Volume
Date                                                                 
2017-05-01  238.679993  238.679993  239.169998  238.199997   66882500
2017-05-02  238.839996  238.770004  238.979996  238.300003   57375700
2017-05-03  238.770004  238.479996  238.880005  237.699997   73137700
2017-05-04  238.830002  238.759995  238.919998  237.779999   61462700
2017-05-05  239.190002  239.699997  239.720001  238.679993   62001300
2017-05-08  239.750000  239.660004  239.919998  239.169998   48385700
2017-05-09  239.960007  239.440002  240.190002  239.039993   51363200
2017-05-10  239.389999  239.869995  239.869995  239.149994   54293800
2017-05-11  239.350006  239.380005  239.570007  238.130005   62358300
2017-05-12  239.089996  238.979996  239.429993  238.669998   53912700
2017-05-15  239.470001  240.300003  240.440002  239.449997   61918900
2017-05-16  240.639999  240.080002  240.669998  239.630005   51241800
2017-05-17  240.080002  235.820007  240.080002  235.750000  172174100
2017-05-18  235.729996  236.770004  237.750000  235.429993  107047700
2017-05-19  237.330002  238.309998  239.080002  237.270004  115011400
2017-05-22  238.899994  239.520004  239.710007  238.820007   61010600
2017-05-23  239.949997  240.050003  240.240005  239.509995   48341700

>>> data['Close'].plot(figsize=(10, 10))
>>> import matplotlib.pyplot as plt
>>> plt.show()
data['Return_Out'] = data['Close'].pct_change()