class Exploring(object):
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
