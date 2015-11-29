class MyInteger(object):
	def set_val(self,val):
		try:
			val = int(val)
		except ValueError:
			return
		self.val = val
	
	def get_val(self):
		return self.val
	
	def increment_val(self):
		self.val = self.val + 1

i = MyInteger()
i.val = "hi"
print i.increment_val()
print 