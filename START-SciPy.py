# -*- coding: utf-8 -*-
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
