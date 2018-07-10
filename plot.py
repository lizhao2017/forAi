# -*- coding: utf-8 -*-0
"""
Created on Thu Jun 28 23:02:48 2018

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

unrate=pd.read_csv('UNRATE.csv')

unrate['DATE']=pd.to_datetime(unrate['DATE'])
print(unrate.head(12))
# =============================================================================
# 
# plt.plot()
# plt.show()
# 
# first_towen=unrate[0:12]
# plt.plot(first_towen['DATE'],first_towen['VALUE'])
# plt.xticks(rotation=45)
# 
# 
# fig=plt.figure(figsize=(6,6))
# ax1=fig.add_subplot(4,3,1)
# ax2=fig.add_subplot(4,3,2)
# ax6=fig.add_subplot(4,3,6)
# =============================================================================
# =============================================================================
# unrate['MONTH']=unrate['DATE'].dt.month
# plt.plot(unrate[0:12]['MONTH'],unrate[0:12]['VALUE'],c='red')
# plt.plot(unrate[12:24]['MONTH'],unrate[12:24]['VALUE'],c='blue')
# plt.show()
# =============================================================================
num_cols=['RT_user_normal','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Starts']
bar_heights=norm_reviews.ix[0,num_cols].values
print(bar_heights)






         