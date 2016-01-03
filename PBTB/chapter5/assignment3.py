import os

class ConfigDict(dict):

	def __init__(self, filename):
		# Store the filename.
		self._filename = filename
		# Check to see if the file exists in the system.
		if os.path.isfile(self._filename):
			# Open the file, and store the file handler object.
			with open(self._filename) as fh:
				# Go through all the lines, split each line, and store the key and value appropriately in the dictionary object.
				for line in fh:
					arr = line.split("=")
					dict.__setitem__(self, arr[0], arr[1].rstrip('\n'))
		else:
			print "The file, '" + filename + "' does not exist in the system."

	def __getitem__(self, key):
		return dict.__getitem__(self, key)

	def __setitem__(self, key, val):
		# Open the file, and store the file handler object.
		with open(self._filename, 'a') as fh:
			# If the key doesn't already exist in the config file, write the key=value combination to it.
			if key not in self:
				# Update the dictionary object as well.
				dict.__setitem__(self, key, val)
				# Update the file.
				self.fh.write(key + "=" + val + '\n')
			else:
				print "The key '" + key + "' already exists in the config file. Skipping..."