from random import randint

class Riddle_Solved_Message():
	success_quips = ["So you did it. Well done. I would have expected a child to work that one out, let alone the world's greatest detective.",
					"Don't get too full of yourself, Dark Knight. It only gets harder from here.",
					"You are performing just below my predicted expectations. At this rate you'll never beat me.",
					"I'd have solved all the puzzles by now.",
					"That one could have been solved by a monkey. But good job, nevertheless.",
					"Easy! Isn't it? Well, we'll see. We'll see.",
					"Bah. Another one of the easy ones. Don't feel too proud, Batman.",
					"Another one? Can it be?...No. There's no way. You can't find them all. It's impossible.",
					"You are beginning to impress me, Batman. You may still reach a level just below my genius one day.",
					"I'm impressed. That was one of the more taxing ones.",
					"I'm losing patience. You are cheating. You must be.",
					"What? you found that one too? Preposterous.",
					"I don't believe it! How did you work that one out?",
					"That one was impossible to solve! How did you do that!?"
	]

	def print_success_message(self):
		print Riddle_Solved_Message.success_quips[randint(0,len(self.success_quips)-1)]
