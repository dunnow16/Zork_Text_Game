#!usr/bin/env python3

from observer_pattern.observer import Observer
from observer_pattern.observable import Observable
from objects.npc import Zombie
from objects.npc import Vampire
from objects.npc import Ghoul
from objects.npc import Werewolf
import random


class House(Observer, Observable):
    """
    House object: A house is initialized with 0-10 monsters of random
    type. It observes monsters living within. The population of the
    monsters is changed when notified of an update event.
    """

    def __init__(self):
        """Initialize the house object."""

        # The total monster count in the house.
        self.__house_monsters = 0
        # A list of all the monsters in the house.
        self.__monsters = []
        # Add 0-10 monsters to the house.
        self.__create_monsters()

    def __create_monsters(self):
        """This function creates the monsters for the house."""

        # The number of types of monsters.
        monster_types = 4
        # The maximum monsters that can be added to the house.
        max_monsters = 10

        for i in range(random.randrange(max_monsters+1)):
            # Choose a random monster.
            r = random.randrange(monster_types)
            if r == 0:  # Create a zombie.
                monster = Zombie()
            elif r == 1:
                monster = Vampire()
            elif r == 2:
                monster = Ghoul()
            elif r == 3:
                monster = Werewolf()
            self.__monsters.append(monster)
            self.__house_monsters = self.__house_monsters + 1

    def get_house_monsters(self):
        """
        Returns the total monster count in the house.

        :return: __total_monsters
        """
        return self.__house_monsters

    def update_observer(self):
        """

        :return:
        """
        print('Monster updated!')

    def update_observable(self):
        """

        :return:
        """
        print('Population updated!')

