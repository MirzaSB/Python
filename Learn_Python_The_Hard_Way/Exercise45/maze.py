import scene
import riddle_solved_message

class Maze():

    riddles = {
        1 : "Where does a 500 pound gorilla sleep? What's worse than a millipede with flat feet? How do you fit 5 elephants into a compact car?",
        2 : "You can only keep yours after you give it to somebody.",
        3 : "I have billions of eyes, yet I live in darkness. I have millions of ears, yet only four lobes. I have no muscle, yet I rule two hemispheres. What am I?"
    }

    riddle_solutions = {
        1 : "DMV",
        2 : "Your word",
        3 : "Human brain"
    }

    def enter(self):

        print "You are at the final stage."
        print "You are in the maze. Get ready Batman!!!!"
        print "\n"

        for x in Maze.riddles:

            print Maze.riddles[x]
            
            action = raw_input("> ")

            if action == Maze.riddle_solutions[x]:
                print "\n"
                riddle_solved_message.Riddle_Solved_Message().print_success_message()
                print "--------------------"
                print "\n"
            else:
                return 'death'

        return 'finished'