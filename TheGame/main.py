from sys import exit
from engine import Engine
from death import Death        
from lastDayOnEarth import LastDayOnEarth
from exploring import Exploring
from deactivation import Deactivation            
from escape import Escape
from mapa import Map    


      
a_map = Map('last_day_on_earth')
a_game = Engine(a_map)
a_game.play()                
