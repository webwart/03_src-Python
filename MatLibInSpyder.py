# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:16:32 2018

@author: raine_kd2ek0t
"""

#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

s = pd.Series([1,3,5,np.nan,6,8])

# Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:

date = pd.date_range('20130101', periods =6)
