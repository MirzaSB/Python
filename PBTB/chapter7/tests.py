import pickle

mylist = ['a', 'b', 'c', 'd']

with open('datafile.txt', 'w') as fh:
	pickle.dump(mylist, fh)


