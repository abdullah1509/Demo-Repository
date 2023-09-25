Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df=pd.read_csv("pydb1.csv")
>>> df
       Name  Age Gender  Income
0     Nihal   23      M   23000
1       Ram   34      M   40000
2       Raj   23      M   47000
3    Sunita   18      F   49000
4      Gita   23      F   24000
5      Sita   34      F   34000
6     Jason   22      M   45000
7  Lagartha   35      F   56000
>>> df.groupby(['Gender'])['Income'].agg(['mean','median'])
           mean   median
Gender                  
F       40750.0  41500.0
M       38750.0  42500.0
