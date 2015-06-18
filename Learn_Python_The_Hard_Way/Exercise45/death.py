from sys import exit
import scene
from random import randint

class Death():

	quips = [
		"Fail! Not so easy now, is it? I think it's time to introduce a little penalty to help you comprehend your ignorance. What shall it be? Oh yes. I've frozen you out, Dark Knight. Frustrating, isn't it? Take some time to wrap your feeble mind around where you went wrong and try again.",
		"Give up? No, really. Give up. You cannot solve this. That is becoming increasingly obvious.",
		"Oh, please. I could have answered that one when I was six years old.",
		"This is embarassing, isn't it? How many times are you going to try and solve that one. Let me give you some time to think about it.",
		"I believe I credited you with more intelligence than I should have. Let's give your brain a rest. It needs it.",
		"So the World's Greatest Detective can't solve the world's simplest riddle? I shouldn't be surprised.",
		"This is hardly a surprise. I always knew I was better than you.",
		"Well, well. So the shaved monkey has failed. How utterly, utterly expected.",
		"What's wrong? Has your primitive brain given up and accepted that I, the Riddler, am better than you?",
		"Riddle me this. What lies on the ground, is full of holes, and gives off a slight burning smell?",
		"You picked wrong, Dark Knight!"
	]

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)
