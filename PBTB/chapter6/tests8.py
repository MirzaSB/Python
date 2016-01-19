mydict = {'a': 1, 'b': 2}

try:
	print 5 / 0
except ZeroDivisionError, e:
	print(e.message)
	print(e.args)
