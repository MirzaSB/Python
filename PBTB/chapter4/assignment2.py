import datetime
import abc

class WriteFile(object):

	def __init__(self, filename):
		self.filename = filename

	@abc.abstractmethod
	def write(self):
		return

	def write_line(self, text_to_write):
		# Open the file, and set the writer object.
		self.writer = open(self.filename, 'a')
		# Write the text, and go to the next line.
		self.writer.write(text_to_write + '\n')
		# Close the writer object.
		self.writer.close()

class LogFile(WriteFile):

	def __init__(self, filename):
		# Invoke the super class to get the __init__ method.
		super(LogFile, self).__init__(filename)

	def get_timestamp(self):
		# Get the timestamp in the expected format, "YYYY-MM-DD hh:mm".
		return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

	'''
	Implementation of the "write" abstract method for LogFile class.
	'''
	def write(self, text_to_write):
		# Concatenate the text with a timestamp and a tab. Then write it to the file.
		self.write_line(self.get_timestamp() + "\t" + text_to_write)

class DelimFile(WriteFile):

	def __init__(self, filename, delim):
		# Invoke the super class to get the __init__ method.
		super(DelimFile, self).__init__(filename)
		self.delim = delim

	'''
	Implementation of the "write" abstract method for DelimFile class.
	'''
	def write(self, list_to_write):
		# Join the list with the expected delimiter, and write it to the file.
		self.write_line(self.delim.join(list_to_write))