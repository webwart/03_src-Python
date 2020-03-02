#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn numpy and matplotlib module
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

s = pd.Series([1,3,5,np.nan,6,8])

# Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:

date = pd.date_range('20130101', periods =6)
