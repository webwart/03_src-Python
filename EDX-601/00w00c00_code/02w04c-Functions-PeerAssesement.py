# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:32:45 2016

@author: raine_u 
@description: Function to calcutatin the sum of 
              1.  area of a regular polygon
              2.  lenth of the polygon's sides.
              3. sum of area (1) and square of length of sides (2)
              The functino then returns:
              sum (3)

"""

import math

def polysum(n, s):
    area =  (0.25*n*s*s)/(math.tan(math.pi/n))
    lengthOfSides = n*s
    sum =  area + (lengthOfSides * lengthOfSides)
    return round(sum, 4)
    