#!usr/bin/env python3

from observer_pattern.observable import Observable
from observer_pattern.observer import Observer
from objects.weapon import Weapon
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

    def set_hp(self, hp):
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

    # How many weapons the player starts with.
    num_start_weapons = 10

    def __init__(self):
        """Initializes the player."""
        super().__init__(random.randint(100, 125),  # Health
                         random.randint(10, 20))    # Attack
        self.__num_weapons = 0  # total weapons
        self.__weapons = []     # player weapon inventory
        # add 10 random weapons to player
        self.__create_start_weapons(Player.num_start_weapons)

    def update_observer(self):  # TODO make observer?
        """Update the player when the game """
        pass

    def __create_start_weapons(self, n):
        """
        Used to create the weapons the player starts the game with.
        """

        # First add the unlimited weapon
        self.__weapons.append(Weapon(0))

        # Create n weapons and add to player's inventory.
        for i in range(n - 1):  # add 9 more random weapons
            # Create one of the 3 weapons (1-3) randomly and add to the
            # players inventory. (not unlimited use weapon)
            wid = random.randint(1, Weapon.num_unique - 1)
            weapon = Weapon(wid)
            self.__weapons.append(weapon)

    def get_num_weapons(self):
        """Returns the number of weapons the player has."""
        return len(self.__weapons)

    def get_weapons(self):
        """Returns the weapon inventory for the player"""
        return self.__weapons

    def select_weapon(self, wid):
        """
        The function returns a weapon from the player's list of weapons.
        If it is discovered that the selected weapon is not in the
        player's inventory, then the one weapon with unlimited uses will
        be returned.
        :param wid: the weapons id that's used to select a weapon from
        the weapons list
        :return: Weapon(): a weapon object from the list of weapons
        """
        for w in self.__weapons:
            if w.get_id() == wid:  # take the first found of wanted type
                # Reduce the number of uses by 1.
                w.use_weapon()
                return w  # we have what we need
        # return hershey kisses if not found
        return self.__weapons[0]

    def remove_weapon(self, weapon):
        """
        This function removes the passed weapon from the player's
        inventory
        :param weapon: Weapon(): object
        :return: none
        """
        if weapon in self.__weapons:
            self.__weapons.remove(weapon)

    def player_defence(self):  # todo
        """
        This function describes what happens when the player is
        attacked. The player is attacked by all the monsters in
        succession in the current house.
        :param
        :return:
        """
        pass


class Monster(Npc, Observable):
    """
    Monster object: Used as a parent to create all monster types. This
    class is only used as a base class to create other monster classes.
    """

    # The total monsters that exist. Not including cured humans.
    total_monsters = 0
    # Allows identification for the monsters.
    monster_id = {0: 'Zombie', 1: 'Vampire', 2: 'Ghoul', 3: 'Werewolf',
                  4: 'Person'}

    def __init__(self, h, s, m):
        """Initialize a generic monster."""
        super().__init__(h, s)
        # Create an observer list for the monster.
        Observable.__init__(self)
        # self.monster_type = monster_type  # type of monster
        # self.immume = []    # weapons immune to
        # self.weakness = []  # weapons weak to
        # self.weak_mult = m  # multiplier of damage for weakness weapons
        self.__mult = m  # damage multiplier dictionary
        # Update the created monster count.
        Monster.total_monsters = Monster.total_monsters + 1

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
        if weapon.get_name() not in self.__mult:
            return 0
        else:
            return self.__mult[weapon.get_name()]

    @staticmethod
    def get_total_monsters():
        """
        Static method that returns the total monsters that exist. Does
        not count monsters that have returned to being human.

        :return: total_monsters: total monsters that exist
        """
        return Monster.total_monsters

    @staticmethod
    def __decrement_monster_count():
        """
        Static method to reduce the count of monsters.
        :return: none
        """

        if Monster.get_total_monsters() <= 0:  # should have won by now
            return
        Monster.total_monsters = Monster.total_monsters - 1

    def monster_defence(self, weapon, attack):
        """
        This function defines what happens when a monster is attacked.
        :param: weapon: Weapon() object
        :param: attack: raw attack value
        :return: none
        """
        # Calculate the damage from player's weapon.
        damage = self.get_multiplier(weapon) * attack * weapon.get_mult()
        print(self.get_multiplier(weapon))
        print(attack)
        print(weapon.get_mult())
        health = self.get_hp() - damage
        self.set_hp(health)
        if health <= 0:
            print('%s defeated! It became a helpful human!'
                  % (Monster.monster_id[self.get_id()]))
            Monster.__decrement_monster_count()
            # Update all houses watching of a monster purified.
            self.update_observable()
        else:
            print("%s hit for %.1f damage, now at %.1f health points."
                  % (Monster.monster_id[self.get_id()], damage, health))


class Zombie(Monster):
    """Zombie object: The weakest monster type."""
    def __init__(self):
        """Initialize the zombie NPC."""
        # self.immume.append("SourStraws")
        # damage multiplier dictionary for zombie
        self.mult = {'HersheyKisses': 1, 'SourStraws': 2,
                     'ChocolateBars': 1, 'NerdBombs': 1}
        self.__id = 0
        super().__init__(random.randint(50, 100),  # Health
                         random.randint(0, 10),    # Attack
                         self.mult)

    def get_id(self):
        """
        Returns the monster's id.
        :return: id: the monster's id number
        """
        return self.__id


class Vampire(Monster):
    """Vampire object: A monster type."""
    def __init__(self):
        """Initialize the vampire NPC."""
        # damage multiplier dictionary
        self.mult = {'HersheyKisses': 1, 'SourStraws': 1,
                     'ChocolateBars': 0, 'NerdBombs': 1}
        self.__id = 1
        super().__init__(random.randint(100, 200),  # Health
                         random.randint(10, 20),    # Attack
                         self.mult)

    def get_id(self):
        """
        Returns the monster's id.
        :return: id: the monster's id number
        """
        return self.__id


class Ghoul(Monster):
    """Ghoul object: A monster type."""
    def __init__(self):
        """Initialize the ghoul NPC."""
        # damage multiplier dictionary
        self.mult = {'HersheyKisses': 1, 'SourStraws': 1,
                     'ChocolateBars': 1, 'NerdBombs': 5}
        self.__id = 2
        super().__init__(random.randint(40, 80),  # Health
                         random.randint(15, 30),  # Attack
                         self.mult)

    def get_id(self):
        """
        Returns the monster's id.
        :return: id: the monster's id number
        """
        return self.__id


class Werewolf(Monster):
    """Werewolf object: A monster type."""
    def __init__(self):
        """Initialize the werewolf NPC."""
        # damage multiplier dictionary
        self.mult = {'HersheyKisses': 1, 'SourStraws': 0,
                     'ChocolateBars': 0, 'NerdBombs': 1}
        self.__id = 3
        super().__init__(200,                    # Health
                         random.randint(0, 40),  # Attack
                         self.mult)

    def get_id(self):
        """
        Returns the monster's id.
        :return: id: the monster's id number
        """
        return self.__id


class Person(Monster):
    """
    Person object: A helpful 'monster' type.
    When a person is created, a monster was just transformed into the
    person. People heal the player by 1 health point per turn.
    The game is won when all monsters are transformed into people.
    """
    def __init__(self):
        """Initialize the person NPC."""
        # People are immune to everything.
        self.mult = {'HersheyKisses': 0, 'SourStraws': 0,
                     'ChocolateBars': 0, 'NerdBombs': 0}
        self.__id = 4
        super().__init__(100,   # Health
                         -1,    # Attack (they heal player)
                         self.mult)

    def get_id(self):
        """
        Returns the monster's id.
        :return: id: the monster's id number
        """
        return self.__id
