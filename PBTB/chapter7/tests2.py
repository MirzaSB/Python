import pickle

with open('datafile.txt') as fh:
	unpickledlist = pickle.load(fh)

print unpickledlist
