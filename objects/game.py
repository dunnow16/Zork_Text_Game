#!usr/bin/env python3

from observer_pattern.observer import Observer
from objects.neighborhood import Neighborhood
from objects.npc import Player
from objects.npc import Monster
from c_functions.getch import _Getch


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

        getch = _Getch()  # allow single-key input
        x = 0  # x position in neighborhood array
        y = 0  # y position in neighborhood array

        # Go one turn at a time as long as at least one monster exists
        # in the neighborhood. Game can also end if the player's health
        # drops to 0.
        print('You wake up in your house at (0,0).')
        print('You must cure your family first before you can move on.')
        # start game at (0,0) house
        h = self.__n.get_house_loc(x, y)
        # Add the game object as an observer of the house.
        h.add_observer(self)
        if h == -1:
            print('Error: exiting game.')
            return

        while Monster.total_monsters > 0:
            # Stay in house until all monsters defeated.
            # End the game if the player losses (HP <= 0).
            while h.get_house_monsters() > 0:
                print('Choose a candy to attack (1,2,3,4): ')
                ch = getch.__call__()  # read a single char input
                while ch not in '1234':
                    print('Please enter a valid character: ')
                    ch = getch.__call__()  # read a single char input
                wid = ord(ch)  # get weapon id from character
                # get weapon from inventory
                w = self.__player.select_weapon(wid - 1)
                # Find how much raw damage is done by the player.
                attack = self.__player.get_strength()
                # The player attacks all monsters.
                h.player_attack(w, attack)
                # Check if the weapon had its last use.
                if w.get_uses() <= 0:
                    self.__player.remove_weapon(w)
                # The player is attacked by all monsters.
                self.__player.player_defence()
            print('House clear of monsters.')
            print('Make your next move (w,a,s,d): ')
            ch = getch.__call__()  # read a single char input
            while ch not in 'wasd':
                print('Please enter a valid character: ')
                ch = getch.__call__()  # read a single char input
            if ch == 'w':
                if (x + 1) < self.__n.get_rows():  # if within bounds
                    x = x + 1  # Move up 1 house row.
                else:  # This is out of bounds.
                    print('')
