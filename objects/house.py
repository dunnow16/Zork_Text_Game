#!usr/bin/env python3

from observer_pattern.observer import Observer
from observer_pattern.observable import Observable
from objects.npc import Zombie
from objects.npc import Vampire
from objects.npc import Ghoul
from objects.npc import Werewolf
from objects.npc import Person
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
        Observable.__init__(self)

    def __create_monsters(self):
        """
        This function creates the monsters for the house.
        :return
        """
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
            # Add this house to the list of observers of the monster.
            monster.add_observer(self)

    def get_house_monsters(self):
        """
        Returns the total monster count in the house.
        :return __total_monsters
        """
        return self.__house_monsters

    def update_observer(self):
        """
        The house updates when a monster is purified. The count of
        monsters is decreased and a person is added to the house in the
        monster's place.
        :return none
        """
        # Remove any monsters with health <= 0.
        for m in self.__monsters:
            if m.get_hp() <= 0:
                self.__monsters.remove(m)
                self.__house_monsters = self.__house_monsters - 1
                # Now add a person to replace the monster.
                person = Person()
                self.__monsters.append(person)

    def update_observable(self):
        """
        The house lets the game know that a monster
        :return:
        """
        print('Population updated!')

    # def enter(self):
    #     """
    #     This function controls what happens when the player enters a
    #     house. The player fights monsters until a health points drop
    #     below 0 or all the monsters in the house are cured humans.
    #     :return none
    #     """
    #
    #     while self.__house_monsters > 0:

    def player_attack(self, weapon, attack):
        """
        This functions describes what happens when the player attacks
        all the monsters in the house.
        :param weapon: Weapon() object
        :param attack: raw damage done by player
        :return none
        """

        # Go through the list of monsters and attack each one with a
        # chosen weapon.
        weapon.use_weapon()
        for m in self.__monsters:
            # Calculate damage and update statistics for monster.
            m.monster_defence(weapon, attack)
