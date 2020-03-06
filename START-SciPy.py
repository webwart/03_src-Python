#!/user/  .in Unix only
# -*- coding: utf-8 -*-

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: -- First: 02-03-2018
#    Goals: Learn RegEx
#      Ref: https://docs.python.org/3.4/howto/regex.html
#      Ref:  
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: broken
#       >N: --

"""
Created on Fri Mar  2 16:58:39 2018

@author: raine_kd2ek0t
"""

# https://www.scipy-lectures.org/index.html -> Tutorials on the scientific Python ecosystem.

from keras.models import Sequential
from keras.layers import Dense, Activation

model2 = Sequential([
    Dense(32, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])
