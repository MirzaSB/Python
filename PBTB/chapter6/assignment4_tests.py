"""
	Usages:
	./test.py						(reads out the entire config dict)
	./test.py thatkey				(prints the value associated with this key)
	./test.py thiskey thisvalue		(sets 'thiskey' and 'thisvalue' in the dict)
"""

import sys
from assignment4 import ConfigDict

cd = ConfigDict('revananalysis.config')

# If 2 arguments on the command line, set a key, and value in the object's dictionary.
if len(sys.argv) == 3:
	key = sys.argv[1]
	value = sys.argv[2]
	print('Writing data: {0}, {1}'.format(key, value))
	cd[key] = value

# If 1 argument on the command line, treat it as a key, and show the value.
elif len(sys.argv) == 2:
	print('reading a value')
	key = sys.argv[1]
	print('the value for {0} is {1}'.format(sys.argv[1], cd[key]))

# If no arguments on the command line, show all keys and values.
else:
	print('keys/values:')
	for key in cd.keys():
		print('		{0}={1}'.format(key, cd[key]))