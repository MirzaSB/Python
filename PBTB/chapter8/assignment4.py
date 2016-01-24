import os
import sys

class ConfigDict(dict):

	def __init__(self, filename):
		# Store the filename.
		self._filename = filename
		if os.path.isfile(filename):
			# Open the file, and store the file handler object.
			with open(self._filename) as fh:
				# Go through all the lines, split each line, and store the key and value appropriately in the dictionary object.
				for line in fh:
					arr = line.split("=", 1)
					dict.__setitem__(self, arr[0], arr[1].rstrip('\n'))
		else:
			raise IOError

	def __getitem__(self, key):
		# Custom exception block that gets the item, and then raises the customized Exception.
		try:
			# Get the property value.
			item = dict.__getitem__(self, key)
			return item
		except KeyError:
			# Raise the custom exception.
			raise ConfigKeyError(self,key)

	def __setitem__(self, key, val):
		# Open the file, and store the file handler object.
		with open(self._filename, 'a') as fh:
			self.fh = fh
			# If the key doesn't already exist in the config file, write the key=value combination to it.
			if key not in self:
				# Update the dictionary object as well.
				dict.__setitem__(self, key, val)
				# Update the file.
				self.fh.write(key + "=" + val + '\n')
			else:
				print "The key '" + key + "' already exists in the config file. Skipping..."

'''
Custom exception for the assignment.
'''
class ConfigKeyError(Exception):

	'''
	Custom __init__ method.
	'''
	def __init__(self, config_dict_instance, *args):
		# Store the ConfigDict instance, and the arguments passed.
		self.config_dict_instance = config_dict_instance
		self.args = args
	
	'''
	Custom __str__ method.
	'''
	def __str__(self):
		# Concatenate the listed arguments so that they can be used in reporting.
		msg_args = ",".join(self.args)
		# Concatenate the available keys in the properties file so they can be used in reporting.
		available_keys = ",".join(self.config_dict_instance.keys())
		# Return the customized error message.
		return "The key(s), '{0}' does not exist in the properties file. The available keys are: {1}.".format(msg_args, available_keys)

#Test
#cd = ConfigDict('somefile.txt')
#print cd['unknown']