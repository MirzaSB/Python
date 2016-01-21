import sys
from assignment5 import ConfigDict

# Initialize a new ConfigDict object using the pickle file, 'test.pickle'.
cd = ConfigDict('test')
# Write the 'firstname' as 'Martin' in the pickle file.
cd['firstname'] = 'Martin'

# This should print "Martin" in the console.
print(cd['firstname'])