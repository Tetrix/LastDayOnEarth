class Escape(object):
    def enter(self):
        print "You find a room with a knife and a machine gun."
        print "what do you take?"
        
        weapon = raw_input("> ")
        print "\n"
        
        if weapon == "knife":
            print "You take the knife and try to kill the"
            print "aliens like a ninja. Your attempt is"
            print "unseccessful and they kill you"
            return 'death'
            
        elif weapon == "machine gun":
            print "You take the machine gun and kill all"
            print "the aliens including the driver of the"
            print "ship. You start searching for instructions"
            print "on how to drive the space ship. You find the"
            print "instructions in the control room and start"
            print "studying them. Lucky for you, you are a"
            print "quick learner and you learn how to drive"
            print "the ship and return back home. GRATZ,"
            print "YOU HAVE FINISHED THE GAME :)\n\n"
            exit(1)
        
        else:
            print "INVALID INPUT"
            return 'escape'        
