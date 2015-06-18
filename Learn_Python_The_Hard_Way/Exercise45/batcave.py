import scene
import riddle_solved_message

class BatCave():

    def enter(self):

        print "You are in the Bat Cave."
        print "\n"
        print "What is the shortest distance between a point in Nome, Alaska and a point in Miami, Florida?"

        action = raw_input("> ")

        if action == "Curved line":
            print "\n"
            riddle_solved_message.Riddle_Solved_Message().print_success_message()
            print "--------------------"
            print "\n"
            return 'gotham_city_bridge'
        else:
            return 'death'