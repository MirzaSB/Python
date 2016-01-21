import os
import sys
import stat
import pickle

class ConfigDict(dict):

	# Declare the path to the config files.
	config_directory = '/Users/mbaig/Workspace/Python/PBTB/chapter7/'

	def __init__(self, config_name):
		# Store the filename.
		self._filename = ConfigDict.config_directory + config_name + ".pickle"
		try:
			# Open the file, and store the file handler object.
			with open(self._filename, 'w') as fh:
				# If the file is not empty.
				if os.stat(self._filename).st_size > 0:
					# Unpickle the pickle file.
					self = pickle.load(fh)
				else:
					# Write an empty dictionary object to the pickle file if it is empty.
					pickle.dump({}, fh)
		# Custom exception block that kills the program when no file is found.			
		except IOError, io:
			print(io.args[1])
			print("The file, '" + self._filename + "' does not exist in the system. Exiting the program...")
			sys.exit(0)

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
			# If the key doesn't already exist in the config file, write the key=value combination to it.
			if key not in self:
				dict.__setitem__(self, key, val)
				# Dump the data into the pickle.
				pickle.dump(self, fh)
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