import math
import os
import sys

import requests

# print(sys.version)
print(sys.executable)



def greet(who_to_greet):
    test = "Test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Corey'))

r = requests.get("https://rainer-warth.eu")
print(r.status_code)
