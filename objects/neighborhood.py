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
        """
        Create a random neighborhood. A grid of houses are created with
        a random number of monsters in each house. As each house is
        created, the game object is added as an observer.
        :return: none
        """
        if len(self.__neighborhood) > 0:  # if list not empty
            self.__neighborhood.clear()  # delete old neighborhood
        self.__neighborhood = \
            [[0 for i in range(self.__cols)]
             for j in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(self.__cols):
                h = House()
                self.__neighborhood[i][j] = h

    def get_rows(self):
        """
        Returns the number of rows in neighborhood.
        :return rows: total rows in the neighborhood
        """
        return self.__rows

    def get_cols(self):
        """
        Returns the number of columns in neighborhood.
        :return columns: total columns in the neighborhood
        """
        return self.__cols

    def get_total_monsters(self):
        """
        Return the total number of monsters in neighborhood.

        :return __total_monsters: total monsters in neighborhood
        """
        return self.__total_monsters

    def get_house_loc(self, x, y):
        """
        This function returns a house object at location (x,y) in the
        neighborhood array.

        :param x: house row
        :param y: house column
        :return House(): the house at location (x,y) in the neighborhood
        array
        """

        # Check if within the bounds of the neighborhood.
        if 0 <= x < self.__rows:
            if 0 <= y < self.__cols:
                return self.__neighborhood[x][y]

        print('Invalid location: No house returned.')
        return -1
