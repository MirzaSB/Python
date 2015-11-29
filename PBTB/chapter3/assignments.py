
class MaxSizeList(object):

	def __init__(self, size):
		self.size = size
		#Initialize a list.
		self.new_list = []

	def push(self, val):
		#Remove the first element in the list if the size goes over.
		if not self.get_size() < self.size:
			self.new_list.pop(0)
		#Append the item to the list.
		self.new_list.append(val)

	def get_list(self):
		#Get all the items in the list.
		return self.new_list

	def get_size(self):
		#Get the current size of the list.
		return len(self.new_list)