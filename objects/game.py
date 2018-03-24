#!usr/bin/env python3

from observer_pattern.observer import Observer
from objects.neighborhood import Neighborhood
from objects.npc import Player
from objects.npc import Monster
from c_functions.getch import _Getch
from objects.weapon import Weapon


class Game(Observer):
    """
    Game class: Object to hold an instance of a neighborhood and a 
    player. Observes houses: when the population changes, the game is
    notified and changes the total monster count for the neighborhood.
    """

    def __init__(self):
        """Class initializer code."""
        self.__n = Neighborhood()
        # The total monster objects created found in the Monster class.
        self.__total_monsters = Monster.total_monsters
        self.__posx = 0  # house x coordinate
        self.__posy = 0  # house y coordinate
        self.__player = Player()  # create player character
        print("Your starting statistics:")
        print('Health Points = %d' % self.__player.get_hp())
        print('Strength      = %d' % self.__player.get_strength())
    
    def update_observer(self):
        """
        Observer update code. This object observes houses. Houses update
        the game object when a monster is changed into a human. This
        causes a decrement of the total monster count. The game is won
        when there are no monsters left.
        :return: none
        """
        self.__total_monsters = self.__total_monsters - 1
        if self.__total_monsters <= 0:  # Winning condition
            print('You Win!\nYour neighborhood is now safe.')

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
                wid = int(ch)  # get weapon id from character

                # get weapon from inventory
                w = self.__player.select_weapon(wid - 1)
                print('You attack with %s!' %
                      Weapon.valid_names[w.get_name()])

                # Find how much raw damage is done by the player.
                attack = self.__player.get_strength()

                # The player attacks all monsters.
                h.player_attack(w, attack)

                # Check if the weapon had its last use.
                if w.get_uses() <= 0:
                    self.__player.remove_weapon(w)
                    print('%s out of uses.' %
                          Weapon.valid_names[w.get_name()])

                # The player is attacked by all monsters.
                h.player_defence(self.__player)

                # Check if game over condition met.
                if self.__player.get_hp() <= 0:
                    print('\nGAME OVER! :(\ntry again?')
                    return

            print('House clear of monsters.\n')
            print('You find some untainted candy and restore your health.\n')
            self.__player.set_hp(125)
            # todo add some new weapons after each house?
            print('Make your next move (w,a,s,d): ')
            ch = getch.__call__()  # read a single char input
            valid = False
            while ch not in 'wasd' or not valid:
                while ch not in 'wasd':
                    print('Please enter a valid character: ')
                    ch = getch.__call__()  # read a single char input
                if ch == 'w':
                    # Check if within bounds for given direction.
                    if (y + 1) < self.__n.get_rows():
                        y = y + 1  # Move up 1 house row.
                        valid = True
                    else:  # This is out of bounds.
                        print('Out of bounds!')
                        ch = ' '
                elif ch == 's':
                    if (y - 1) >= 0:  # if within bounds
                        y = y - 1  # Move up 1 house row.
                        valid = True
                    else:  # This is out of bounds.
                        print('Out of bounds!')
                        ch = ' '
                elif ch == 'a':
                    if (x - 1) >= 0:  # if within bounds
                        x = x - 1  # Move up 1 house row.
                        valid = True
                    else:  # This is out of bounds.
                        print('Out of bounds!')
                        ch = ' '
                elif ch == 'd':
                    if (x + 1) < self.__n.get_cols():
                        x = x + 1  # Move up 1 house row.
                        valid = True
                    else:  # This is out of bounds.
                        print('Out of bounds!')
                        ch = ' '

            # Go to the next house.
            h = self.__n.get_house_loc(x, y)

            # Add the game object as an observer of the house.
            if h == -1:
                print('Error: exiting game.')
                return

            h.add_observer(self)
            print('You enter house (%d, %d)\n' % (x, y))
