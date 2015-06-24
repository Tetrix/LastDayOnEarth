class LastDayOnEarth(object):
    def enter(self):
        print "A giant asteroid has hit the Earth."
        print "The asteroid has bought with it aliens."
        print "The aliens slayed every living thing on Earth, except you."
        print "You are the sole survivor hiding in a cave."
        print "After months of hiding, the aliens found you."
        print "You have 2 options:\n1.Make peace \n2.Fight them"
        
        action = raw_input("> ")
        print "\n"
        
        if action =="2":
            print "You take the spear which you made last month"
            print "and stab one of the aliens."
            print "You make the alins angry and they frie"
            print "your head with a lazer"
            return 'death'
            
        elif action == "1":
            print "Aliens take you with them on their spaceship."
            print "There you are held as a hostage for 3 years"
            print "and numerous experiments are made on your body."
            return 'exploring'
        
        else:
            print "INVALID INPUT"
            return 'last_day_on_earth'   
