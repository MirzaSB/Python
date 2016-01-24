import timeit

def testme(this_dict, key):
	return this_dict[key]

print timeit.timeit("testme(mydict, key)", setup="from __main__ import testme; mydict = {'a': 1, 'b': 2, 'c': 3}; key='c'", number=10000)