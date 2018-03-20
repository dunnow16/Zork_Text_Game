#!usr/bin/env python3


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

    def __init__(self, n, m, u):
        """Initialize the weapon object."""
        if n in Weapon.valid_names:
            self.name = n      # weapon name
            self.mult = m      # attack multiplier
            self.num_uses = u  # number of uses for weapon
        else:
            self.name = 'invalid'
            self.mult = 0
            self.num_uses = 0

    def get_uses(self):
        """Returns the number of uses the weapon has left."""
        if self.name == "HersheyKisses":  # unlimited use
            return 1

        return self.num_uses
