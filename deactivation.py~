from random import randint

class Deactivation(object):
    def enter(self):
        print "You have 5 tries for deactivate the bomb."
        code = "%d" % (randint(1,9))
        guess = raw_input("> ")
        guesses = 0
        
        while guess != code and guesses <4:
            print "ERROR!!!"
            guesses +=1
            guess = raw_input("> ")
        
        if guess == code:
            print "You successfully deactivated the bomb and"
            print "you are safe (for now). You start making"
            print "plans for your return home."
            return 'escape'
        
        else:
            print "The bomb explodes and scatters your body"
            print "in the room."
            return 'death'    
