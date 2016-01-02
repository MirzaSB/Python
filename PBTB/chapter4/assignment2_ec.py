import datetime

class WriteFile(object):

	def __init__(self, filename, formatter):
		# Open the file, and set the formatter type.
		self.writer = open(filename, 'w')
		self.formatter = formatter()

	'''
	Common method that does the writing.
	'''
	def write(self, text_to_write):
		# Invoke the appropriate "format" method first, and then write the processed output to the file.
		# Then go to the next line.
		self.writer.write(self.formatter.format(text_to_write) + "\n")

	def close(self):
		# Close the writer object.
		self.writer.close()

class CSVFormatter(object):

		def __init__(self):
			# Set the specific delimiter; comma.
			self.delim = ','

		'''
		Formatter for CSV files.
		'''
		def format(self, list_to_format):
			# Initialize new list to store the processed elements.
			formatted_list = []
			# Surround double quotes around the element that has a comma.
			for element in list_to_format:
				if self.delim in element:
					element = '\"' + element + '\"'
					formatted_list.append(element)
				else:
					# Put the element in the new list otherwise.
					formatted_list.append(element)
			# Return the processed list.
			return self.delim.join(formatted_list)

class LogFormatter(object):

	def get_timestamp(self):
		# Get the timestamp in the expected format, "YYYY-MM-DD hh:mm".
		return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

	'''
	Formatter for Log files.
	'''
	def format(self, text_to_format):
		# Concatenate the timestamp to the text and return it.
		return self.get_timestamp() + "\t" + text_to_format