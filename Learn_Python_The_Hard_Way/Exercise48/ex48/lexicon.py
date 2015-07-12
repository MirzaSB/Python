def convert_number(s):
	try:
		return int(s)
	except:
		return None

def scan(param):
	DIRECTIONS = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
	VERBS = ["go", "stop", "kill", "eat"]
	STOPS = ["the","in","of","from","at","it"]
	NOUNS = ["door","bear","princess","cabinet"]
	#Initialize the results list to return.
	results_list = []
	#Split the passed argument.
	params = param.split()
	
	for s in params:
		#Append the "direction" tuple.
		if s in DIRECTIONS:
			results_list.append(('direction', s))
		#Append the "verb" tuple.
		elif s in VERBS:
			results_list.append(('verb', s))
		#Append the "stop" tuple.
		elif s in STOPS:
			results_list.append(('stop', s))
		#Append the "noun" tuple.
		elif s in NOUNS:
			results_list.append(('noun', s))
		#Append the "number" tuple.
		elif s.isdigit():
			results_list.append(('number', convert_number(s)))
		#Append the "error" tuple.
		else:
			results_list.append(('error', s))

	#Return the processed list.
	return results_list