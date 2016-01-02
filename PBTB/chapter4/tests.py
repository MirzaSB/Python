# Inherits from the 'object' class (will discuss shortly)
class Date(object):
	def get_date(self):
		return "2014-10-13"

	def test_inheritance(self):
		return "this tests inheritance"

class Time(Date):
	def get_time(self):
		return "08:13:17"

dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())
print(tm.test_inheritance())