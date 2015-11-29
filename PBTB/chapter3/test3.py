class MyNum(object):
	def __init__(self, value):
		print "calling__init__"
		try:
			value = int(value)
		except ValueError:
			value = 0
		self.value = value

	def increment(self):
		self.val = self.val + 1

aa = MyNum('hello')
bb = MyNum(100)
aa.increment()
bb.increment()
print aa.val
print bb.val