#MyList inherits from "list" object but indexes from 1 instead of 0!

class MyList(list): # Inherit from list
	
	def __getitem__(self, index):
		if index == 0: raise IndexError
		if index > 0: index = index - 1
		return list.__getitem__(self, index) # This method is called when we access a value with sunscript (x[1], etc.)

	def __setitem__(self, index, value):
		if index == 0: raise IndexError
		if index > 0: index = index -1
		list.__setitem__(self, index, value)

x = MyList(['a','b','c'])	# __init__() inherited from the built-in list.

print x 			# __repr__() inherited from the built-in list.

x.append('spam')	# append() inherited from the built-in list.

print x[1]			# 'a' (MyList.__getitem__ customizes list superclass method)
					# index is 1, but reflects 0!

print x[4]			# 'spam' (index is 4 but reflects 3!)
