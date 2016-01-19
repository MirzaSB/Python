mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key = raw_input('please input a key: ')

try:
	print('testing for error')
	print('the value for {0} is {1}'.format(key, mydict[key]))
	print('everything is ok')
except KeyError:
	print('trapped error')
	print('the key {0} does not exist'.format(key))

print('program continues')
