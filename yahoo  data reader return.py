Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from pandas_datareader import data as pdr
>>> import matplotlib.pyplot as plt
>>> import fix_yahoo_finance # must pip install first
>>> data = pdr.get_data_yahoo('EFL.TO','2017-05-01','2017-06-02')[['Open','Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/EFL.TO?period1=1493611200&period2=1496376000&interval=1d&events=history&crumb=vcz5.EdLXnK
>>> data1 = pdr.get_data_yahoo('EFL.TO','2017-05-01','2017-06-02')[['Open','Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/EFL.TO?period1=1493611200&period2=1496376000&interval=1d&events=history&crumb=vcz5.EdLXnK
>>> data2 = pdr.get_data_yahoo('^GSPTSE','2017-05-01','2017-06-02')[['Open','Close','High','Low','Volume']]
https://query1.finance.yahoo.com/v7/finance/download/^GSPTSE?period1=1493611200&period2=1496376000&interval=1d&events=history&crumb=vcz5.EdLXnK
>>> data2
                    Open         Close          High           Low     Volume
Date                                                                         
2017-05-01  15601.700195  15575.599609  15605.900391  15561.599609  202493500
2017-05-02  15590.299805  15619.700195  15656.000000  15565.700195  254795900
2017-05-03  15591.200195  15543.099609  15639.700195  15537.500000  240566200
2017-05-04  15510.000000  15396.700195  15523.900391  15367.400391  275477100
2017-05-05  15441.599609  15582.000000  15594.500000  15423.299805  213120600
2017-05-08  15624.900391  15652.099609  15661.299805  15592.500000  199934100
2017-05-09  15644.099609  15569.200195  15672.200195  15516.700195  209499100
2017-05-10  15567.500000  15633.200195  15643.099609  15565.900391  245801500
2017-05-11  15616.799805  15550.599609  15636.400391  15526.000000  255468800
2017-05-12  15550.799805  15537.900391  15603.000000  15505.099609  200337600
2017-05-15  15625.700195  15629.500000  15674.599609  15613.799805  207388000
2017-05-16  15650.000000  15543.299805  15700.599609  15542.599609  211461200
2017-05-17  15501.599609  15273.700195  15501.599609  15273.700195  253234300
2017-05-18  15229.299805  15277.200195  15336.599609  15164.700195  234164500
2017-05-19  15347.000000  15458.500000  15469.900391  15334.900391  209881600
2017-05-23  15521.099609  15476.900391  15538.799805  15465.900391  225545100
2017-05-24  15470.500000  15419.500000  15470.500000  15326.900391  204849000
2017-05-25  15463.599609  15410.700195  15504.000000  15340.299805  191402900
2017-05-26  15429.000000  15416.900391  15429.400391  15368.299805  151789900
2017-05-29  15420.299805  15421.900391  15460.500000  15405.299805   58843500
2017-05-30  15396.200195  15372.400391  15429.000000  15360.900391  161106700
2017-05-31  15374.400391  15349.900391  15382.099609  15254.099609  374619900
2017-06-01  15363.099609  15469.900391  15493.900391  15337.500000  224803200
2017-06-02  15466.099609  15442.799805  15466.099609  15419.400391  179056300
 
>>> data1['Return_Out_EFL'] = data1['Close'].pct_change()
>>> data2['Return_Out_Tsx'] = data2['Close'].pct_change()

>>> data1['Return_Out_EFL'].plot(legend=True)
<matplotlib.axes._subplots.AxesSubplot object at 0x00000000081B9208>
>>> data2['Return_Out_Tsx'].plot(legend=True)
<matplotlib.axes._subplots.AxesSubplot object at 0x00000000081B9208>
>>> plt.legend()
<matplotlib.legend.Legend object at 0x0000000007D739B0>
>>> plt.show()

>>> import numpy as np
>>> np.mean(data1['Return_Out_EFL'])
-0.004606826049223892