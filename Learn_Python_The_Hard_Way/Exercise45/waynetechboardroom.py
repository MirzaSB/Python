import scene
import riddle_solved_message

class WayneTechBoardRoom():

    def enter(self):

        print "You are at the Wayne Tech board room."
        print "\n"
        print "Why do million dollar deals breakdown in the wasteland?"

        action = raw_input("> ")

        if action == "Clubs not doing good business lately":
            print "\n"
            riddle_solved_message.Riddle_Solved_Message().print_success_message()
            print "--------------------"
            print "\n"
            return 'batcave'
        else:
            return 'death'