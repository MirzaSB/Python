def make_delim_line(list_to_join, delim):
	formatted_line = delim.join(list_to_join)
	return formatted_line

fline = make_delim_line(100, ',')
