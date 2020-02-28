# Reference: Michel Kennedy - https://www.youtube.com/watch?v=rFxXDO8-keg
# Description:  Learn XML and use of OS.path from youtube video
# 
# Example xml file:
# C:\Users\Public\Documents\Pub_CodeDev\TestData\XML\reed.xml
#

import os
from xml.etree import ElementTree

file_name = 'reed.xml'
dir_TestData = os.path.abspath('C:\\Users\\Public\\Documents\\Pub_CodeDev\TestData\\XML\\')

full_file = os.path.abspath(os.path.join(dir_TestData, file_name))

print("Loading file: ", full_file)

dom = ElementTree.parse(full_file)
print(dom)


## find and print all <title> in all <course>
'''
courses = dom.findall('course/title')
for c in courses:
    print(c.text)
'''

## find all <title>, <crse>, <days>

courses = dom.findall('course')



for c in courses:
    title = c.find('title').text
    num = c.find('crse').text
    days = c.find('days').text
    startTime = c.find('time/start_time').text

    print(' * {} [{}] -{}- {}'.format( num, days, startTime, title))

    
    
