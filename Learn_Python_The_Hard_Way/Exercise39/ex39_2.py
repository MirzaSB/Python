import hashmap

#create a mapping of sate to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

#Create a basic set of states and some cities in them.
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

#Add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

#Print out some cities
print '_' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

#print some states
print "_" * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

#Do it by using the state then cities dict
print '_' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Floruda has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

#Print every state abbreviation
print '_' * 10
hashmap.list(states)

#Print every city in the state
print '_' * 10
hashmap.list(cities)

print '_' * 10
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas."

# Default values using || = with the nil result
# Can you do this in one line?
city = hashmap.get(cities, 'TX', "Does Not Exist")
print "The city for the state 'TX' is: %s" % city
