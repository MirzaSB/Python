import re

def process_date(this_date):
	
	# This RegEx makes sure that this date is in YYYY-MM-DD format.
	if not re.search(r'^\d\d\d\d-\d\d-\d\d$', this_date):
		raise ValueError('please submit the date in YYYY-MM-DD format')
	print 'the submitted date is {0}'.format(this_date)

process_date('1980-01-03')
print; print
process_date('1/3/1980')
