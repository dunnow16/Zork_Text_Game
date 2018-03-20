#!usr/bin/env python3

from observer_pattern.observable import Observable
from observer_pattern.observer import Observer
import random


class Npc(object):
    """
    NPC object: (non-playable character) Used to create the different
    characters in the game. Also used to create the player character,
    which is playable.
    """

    def __init__(self, h, s):
        """NPC initialization code."""
        self.__hp = h        # health points
        self.__strength = s  # how much damage is done before multiplier

    def get_hp(self):
        """Returns the current NPC health points (hp)."""
        return self.__hp

    def __set_hp(self, hp):
        """Set the npc health points."""
        self.__hp = hp

    def get_strength(self):
        """Returns the NPC strength."""
        return self.__strength

    def __set_strength(self, s):
        """Set the npc strength."""
        self.__strength = s


class Player(Npc, Observer):
    """
    Player object: The character the player of the game uses to travel
    the neighborhood and fight monsters with candy in houses. The player
    can hold 10 weapons at a time.
    """

    num_weapons = 0

    def __init__(self):
        """Initializes the player."""
        super().__init__(random.randint(100, 125),  # Health
                         random.randint(10, 20))    # Attack
        self.num_weapons = 0  # total weapons
        # TODO add 10 random weapons
        for i in range(9):
            self.__weapons = []

    def update_observer(self):  # TODO make observer?
        """Update the player when the game """
        pass


class Monster(Npc, Observable):
    """
    Monster object: Used as a parent to create all monster types. This
    class is only used as a base class to create other monster classes.
    """
    def __init__(self, h, s, m):
        """Initialize a generic monster."""
        super().__init__(h, s)
        # self.monster_type = monster_type  # type of monster
        # self.immume = []    # weapons immune to
        # self.weakness = []  # weapons weak to
        # self.weak_mult = m  # multiplier of damage for weakness weapons
        self.__mult = m  # damage multiplier dictionary

    # def update_observable(self):
    #     """
    #     Update for monster object. This is called when the monster dies.
    #     """
    #     pass

    def get_multiplier(self, weapon):
        """
        Use the multiplier dictionary to return the damage multiplier.
        This function returns 0 if the weapon does not harm the monster
        or the weapon is not part of the list (may not exist).
        """

        # Check if weapon is in the dictionary. If not, return 0.
        # If found, return the multiplier.
        if weapon not in self.__mult:
            return 0
        else:
            return self.__mult[weapon]


class Zombie(Monster):
    """Zombie object: The weakest monster type."""
    def __init__(self):
        """Initialize the zombie NPC."""
        # self.immume.append("SourStraws")
        # damage multiplier dictionary for zombie
        self.mult = {'HersheyKisses': 1, 'SourStraws': 2,
                     'ChocolateBars': 1, 'NerdBombs': 1}
        super().__init__(random.randint(50, 100),  # Health
                         random.randint(0, 10),    # Attack
                         self.mult)


class Vampire(Monster):
    """Vampire object: A monster type."""
    def __init__(self):
        """Initialize the vampire NPC."""
        # damage multiplier dictionary
        self.mult = {'HersheyKisses': 1, 'SourStraws': 1,
                     'ChocolateBars': 0, 'NerdBombs': 1}
        super().__init__(random.randint(100, 200),  # Health
                         random.randint(10, 20),    # Attack
                         self.mult)


class Ghoul(Monster):
    """Ghoul object: A monster type."""
    def __init__(self):
        """Initialize the ghoul NPC."""
        # damage multiplier dictionary
        self.mult = {'HersheyKisses': 1, 'SourStraws': 1,
                     'ChocolateBars': 1, 'NerdBombs': 5}
        super().__init__(random.randint(40, 80),  # Health
                         random.randint(15, 30),  # Attack
                         self.mult)


class Werewolf(Monster):
    """Werewolf object: A monster type."""
    def __init__(self):
        """Initialize the werewolf NPC."""
        # damage multiplier dictionary
        self.mult = {'HersheyKisses': 1, 'SourStraws': 0,
                     'ChocolateBars': 0, 'NerdBombs': 1}
        super().__init__(200,                    # Health
                         random.randint(0, 40),  # Attack
                         self.mult)
