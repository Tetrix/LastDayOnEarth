from random import randint

class Death(object):
    choices = [
            "You died. You suck at thi game!",
            "Come on, seriously! Is it that hard!?!",
            "My grandmother plays better than you!"
        ]
    def enter(self):
        print Death.choices[randint(0,len(self.choices)-1)]
        exit(1)
