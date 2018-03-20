#!usr/bin/env python3

from objects.house import House


class Neighborhood(object):
    """
    Neighborhood object: holds a grid of house objects. Also keeps
    track of data related to the whole neighborhood object, such
    as the total number of monsters.
    """

    def __init__(self):
        """Initialize a random neighborhood."""
        self.__neighborhood = []
        self.__rows = 5  # may make random later
        self.__cols = 5
        self.create_neighborhood()
        self.__total_monsters = 0

    def create_neighborhood(self):
        """Create a random neighborhood."""
        if len(self.__neighborhood) > 0:  # if list not empty
            self.__neighborhood.clear()  # delete old neighborhood
        self.__neighborhood = \
            [[0 for i in range(self.__cols)]
             for j in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__neighborhood[i][j] = House()

    def get_rows(self):
        """Returns the number of rows in neighborhood."""
        return self.__rows

    def get_cols(self):
        """Returns the number of columns in neighborhood."""
        return self.__cols

    def get_total_monsters(self):
        """Return the total number of monsters in neighborhood."""
        return self.__total_monsters
