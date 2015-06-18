import scene
import riddle_solved_message

class GothamCityBridge():

    def enter(self):

        print "You are at the Gotham City Bridge."
        print "\n"
        print "When is the Minotaur's owner as high as an elephant's eye?"

        action = raw_input("> ")

        if action == "Maze":
            print "\n"
            riddle_solved_message.Riddle_Solved_Message().print_success_message()
            print "--------------------"
            print "\n"
            return 'maze'
        else:
            return 'death'