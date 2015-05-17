numbers = []

def whilefunction(x):
	i = 0
	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

whilefunction(6)

print "The numbers: "

for num in numbers:
	print num
