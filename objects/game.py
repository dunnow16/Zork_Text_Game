#!usr/bin/env python3

from observer_pattern.observer import Observer
from objects.neighborhood import Neighborhood
from objects.npc import Player


class Game(Observer):
    """
    Game class: Object to hold an instance of a neighborhood and a 
    player. Observes houses: when the population changes, the game is
    notified and changes the total monster count for the neighborhood.
    """

    def __init__(self):
        """Class initializer code."""
        self.__n = Neighborhood()
        self.__total_monsters = 0
        self.__posx = 0  # house x coordinate
        self.__posy = 0  # house y coordinate
        self.__player = Player()  # create player character
        print("Your starting statistics:")
        print('Health Points = %d' % self.__player.get_hp())
        print('Strength      = %d' % self.__player.get_strength())
    
    def update_observer(self):
        """Observer update code. This object observes houses."""
        pass

    def get_total_monsters(self):
        """Return the total number of monsters in neighborhood."""
        return self.__total_monsters

    def get_positionx(self):
        """Return the current row position of player."""
        return self.__posx

    def get_positiony(self):
        """Return the current column position of player."""
        return self.__posy

    def play(self):
        """
        This function controls gameplay. The game runs until the
        player wins or looses.
        """
        pass
