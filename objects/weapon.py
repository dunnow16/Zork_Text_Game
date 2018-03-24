#!usr/bin/env python3

import random


class Weapon(object):
    """
    Weapon object: used as a base to create all weapons used by the
    player object to fight monster objects.
    """

    # Define valid weapon name and provide print friendly version.
    valid_names = {'HersheyKisses': 'Hershey Kisses',
                   'SourStraws': 'Sour Straws',
                   'ChocolateBars': 'Chocolate Bars',
                   'NerdBombs': 'Nerd Bombs'}
    # Define weapon id for each weapon. Used to help create new ones.
    weapon_id = {0: 'HersheyKisses', 1: 'SourStraws',
                 2: 'ChocolateBars', 3: 'NerdBombs'}
    # Define the starting uses for each weapon. Used to create new ones.
    start_uses = {0: 1, 1: 2, 2: 4, 3: 1}
    # The number of unique weapons in the game.
    num_unique = 4  # Update if add new weapons.

    def __init__(self, wid):
        """Initialize the weapon object."""
        if 0 <= wid < Weapon.num_unique:
            self.__wid = wid
            self.__name = Weapon.weapon_id[wid]  # weapon name
            if self.__set_mult(wid) == -1:       # if error
                self.__mult = 1.0   # must not have been defined yet
            # Define number of uses for the weapon.
            self.___num_uses = Weapon.start_uses[wid]
        else:
            self.__wid = -1
            self.__name = 'error'
            self.__mult = 0
            self.__num_uses = 0

    def __set_mult(self, wid):
        """
        Sets the multiplier for a weapon.
        The multiplier is defined to be within a certain range for most
        weapons, so update this function if any new weapons are added.
        :param wid: the weapon id
        :return error_code: 0 if no error, -1 if error
        """

        defined_weapons = 4  # number of multiplier assignments defined

        if 0 <= wid < defined_weapons:
            if wid == 0:    # HersheyKisses: 1
                self.__mult = 1
            elif wid == 1:  # SourStraws: 1 - 1.75
                # Choose random multiplier from 1 to 1.75 in increments
                # of 0.05.
                self.__mult = random.uniform(1.00, 1.75)
                print(self.__mult)
            elif wid == 2:  # ChocolateBars: 2 - 2.4
                self.__mult = random.uniform(2.00, 2.40)
                print(self.__mult)
            elif wid == 3:  # NerdBombs: 3.5 - 5
                self.__mult = random.uniform(3.50, 5.00)
                print(self.__mult)
        else:
            return -1  # error code

        return 0

    def get_mult(self):
        """
        Gets the multiplier for a weapon.
        :return self.__mult: the weapons damage multiplier
        """
        return self.__mult

    def get_uses(self):
        """
        Returns the number of uses the weapon has left.
        :return self.__num_uses: number of uses weapon has left
        """

        if self.get_name() == "HersheyKisses":  # unlimited use
            return 1

        return self.__num_uses

    def get_name(self):
        """
        Gets the non-print friendly name for a weapon used in the code.
        :return self.__name: the weapon's name
        """
        return self.__name

    def get_id(self):
        """
        Returns the id of the weapon.
        :return: self.__wid: the weapons id
        """
        return self.__wid

    def print_name(self):
        """
        Prints the weapon name.
        :return none
        """
        if self.__name in Weapon.valid_names:
            print(Weapon.valid_names[self.__name])
        else:
            print("Error: Weapon not found!")

    def use_weapon(self):
        """
        Defines what happens when a weapon is used.
        :return none
        """

        if self.__wid == 0:  # unlimited uses for Hershey Kisses
            return
        elif self.__wid not in Weapon.weapon_id:
            return
        self.__num_uses = self.__num_uses - 1  # reduce uses count by 1
