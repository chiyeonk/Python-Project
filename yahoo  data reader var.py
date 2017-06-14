Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from scipy.stats import norm
>>> from pandas_datareader import data as pdr
>>> import fix_yahoo_finance # must pip install first
>>> data = pdr.get_data_yahoo('EFL.TO','2017-05-01','2017-06-02')[['Open','Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/EFL.TO?period1=1493611200&period2=1496376000&interval=1d&events=history&crumb=zYBC0fyL6oL
>>> P = 10000
>>> c = 0.99
>>> data['Return_Out'] = data['Close'].pct_change()
>>> mu=np.mean(data['Return_Out'])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    mu=np.mean(data['Return_Out'])
NameError: name 'np' is not defined
>>> import numpy as np
>>> mu=np.mean(data['Return_Out'])
>>> sigma = np.std(data['Return_Out'])
>>> def var_cov_var(P, c, mu, sigma):
    """
    Variance-Covariance calculation of daily Value-at-Risk
    using confidence level c, with mean of returns mu
    and standard deviation of returns sigma, on a portfolio
    of value P.
    """
    alpha = norm.ppf(1-c, mu, sigma)
    return P - P*(alpha + 1)

>>> var = var_cov_var(P, c, mu, sigma)
>>> var
1524.37251897848
>>> norm
<scipy.stats._continuous_distns.norm_gen object at 0x0000000005128CF8>
>>> import matplotlib.pyplot as plt
>>> norm
<scipy.stats._continuous_distns.norm_gen object at 0x0000000005128CF8>
>>> plt.show()
>>> k=data['Return_Out']

>>> k.hist() 
>>> plt.show()
>>> 
