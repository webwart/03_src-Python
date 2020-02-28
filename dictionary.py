#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn dictionary
#      Ref: http://learnpythonthehardway.org/book/ex39.html
#      Ref: Frank from Udemy
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------ 




# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print( '-' * 10 )
print( "NY State has: ", cities['NY'] )
print( "OR State has: ", cities['OR'] )

# print some states
print( '-' * 10 )
print( "Michigan's abbreviation is: ", states['Michigan'] )
print( "Florida's abbreviation is: ", states['Florida'] )

# do it by using the state then cities dict
print( '-' * 10 )
print( "Michigan has: ", cities[states['Michigan']] )
print( "Florida has: ", cities[states['Florida']] )

# print every state abbreviation
print( '-' * 10 )
for state, abbrev in states.items():
    print( "%s is abbreviated %s" % (state, abbrev) )

# print( every city in state
print( '-' * 10 )
for abbrev, city in cities.items():
    print( "%s has the city %s" % (abbrev, city)  )

# now do both at the same time
print( '-' * 10 )
for state, abbrev in states.items():
    print( "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]) )

print( '-' * 10 )
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print( "Sorry, no Texas." )

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print( "The city for the state 'TX' is: %s" % city )

# Example added by RaKaWa

dict =  { "A" :  "Adenin" , "G" :  "guanin" , "C" :  "Cytoin" , "T" : "Thymin" }
print( '-' * 10 )
print("== Rainer's example ==")
print("A" in dict)
print("Adenin" in dict)


#%%
# Ref: Udemy - Frank - ML, Data Science and DL with Python
# Like a map or hash table in other languages

captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Siskl"
captains["Voyager"] = "Janeway"

print(captains["Voyager"]) 


# This will through a KeyError exception
# print (captains["NY-01"])

# .... the better way to do it
print(captains.get("NY-01"))

for ship , captain in captains.items():
    print(ship , " : " ,  captain) 



#%%
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
