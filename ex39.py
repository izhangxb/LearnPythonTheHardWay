# create a mapping of state to abbreviation
states = {
    'Pregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Mechigan':'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA':'san francisico',
    'MI':'Detroit',
    'FL':'jacksonville'
}

# add some more cities
cities['NY'] = "New York"
cities['OR'] = "Portland"

# print out some cities
print '=' * 10
print "NY State has :", cities['NY']
print "OR State has:", cities['OR']

#print some states
print '=' * 10
print "Michigan's abbreviation is :" , states['Mechigan']
print "Florida's abbreviation is :", states['Florida']

# do it by using the state then cities dict
print '=' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '=' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# new do both at same time
print '=' * 10
for state, abbrev in states.items():
    print '%s state is abbreviated %s and has city %s' % (state, abbrev, cities[abbrev])

print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not states:
    print  "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print " the city for the state 'TX' is : %s" % city

