from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This class is not yet defined"
        exit (1)
        
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print "\n------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
class Death(Scene):
    choices = [
            "You died. You suck at thi game!",
            "Come on, seriously! Is it that hard!?!",
            "My grandmother plays better than you!"
        ]
    def enter(self):
        print Death.choices[randint(0,len(self.choices)-1)]
        exit(1)
        
class LastDayOnEarth(Scene):
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
            
class Exploring(Scene):
    def enter(self):
       print "One morning you wake up in the room"
       print "where you are held and realize that noone"
       print "is guarding the door. You step outide the"
       print "room and start exploring the spaceship."
       print "You enter a room where you find papers on"
       print "which are written their plans about you."
       print "In the papers you find out that you have a bomb"
       print "planted in your body. You have 2 options."
       print "1. To search for the device to deactivate the bomb"
       print "2. To ignore the fact that you have a bomb in your"
       print "body"
     
       decision = raw_input("> ")
       print "\n"
       
       if decision == "2":
           print "You continue wandering around for 10"
           print "more minutes until the bomb explodes"
           print "and you die"
           return 'death'
       
       elif decision == "1":
           print "You are in panic and start searching the"
           print "rooms for the device. After you found the"
           print "device you see a display on it where you"
           print "have to enter one digit to deactivate the"
           print "bomb"
           return 'deactivation'
       
class Deactivation(Scene):
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
            
class Escape(Scene):
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
        
class Map(object):

    scenes = {
        'last_day_on_earth': LastDayOnEarth(),
        'death': Death(),
        'exploring':Exploring(),
        'escape':Escape(),
        'deactivation':Deactivation()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map('last_day_on_earth')
a_game = Engine(a_map)
a_game.play()                
