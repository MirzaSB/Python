from sys import exit

def room1():
	print "I have billions of eyes, yet I live in darkness. I have millions of ears, yet only four lobes. I have no muscle, yet I rule two hemispheres. What am I?"
	
	choice = raw_input("> ")
	if choice.lower() == "brain":
		print "SUCCESS. Moving on to the next room."
	else:
		dead("You failed in room 1.")

def room2():
	
	print "What is the beginning of eternity, the end of time and space, the beginning of every end and the end of every race?"

	choice = raw_input("> ")
	if choice.lower() == "e":
		print "SUCCESS. You won."
	else:
		dead("You failed in room 2.")

def dead(why):
	print why, "Good job! You are dead."
	exit(0)

def start():
	print "Solve the first riddle."
	room1()
	print "Solve the second riddle."
	room2()


start()


