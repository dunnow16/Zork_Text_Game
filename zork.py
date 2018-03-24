#!usr/bin/env python3

from c_functions.getch import _Getch
from objects.game import Game
from objects.npc import Player
from observer_pattern.observer import Observer
from observer_pattern.observable import Observable
from objects.neighborhood import Neighborhood
from objects.house import House
import objects.house
from objects.npc import Npc
import objects.weapon


if __name__ == "__main__":
    """
    Author: Owen Dunn
    Date:   3/19/18
    
    Zork: Text-Based Game
    A 5x5 neighborhood of houses has a problem. People have turned into
    horrible monsters. Your goal is to transform all monsters back to 
    people by throwing different types of candy at them to bring them 
    (your weapons). The weapons have different attack multipliers. Some 
    monsters are weak against certain types of candy, while immune to
    other types. You, as well as all npcs, have a certain amount of
    health (hitpoints) and attack level. You must clear a house of all 
    monsters before moving to a different house. Use 'w' to go north 
    one house, 'a' to go west, 'd' to go east, and 's' to go south.
    """

    print('===========================ZORK===========================')
    print(' ')
    print('A 5x5 neighborhood of houses has a problem. People have')
    print('turned into horrible monsters. Your goal is to transform')
    print('all monsters back to people by throwing different types')
    print('of candy at them. The candy types have different attack')
    print('multipliers. Some monsters are weak against certain types')
    print('of candy and immune to other types.') 
    print('You, as well as all npcs, have a certain amount of')
    print('hitpoints and attack level.')
    print('You must clear a house of all monsters before moving to a')
    print('different house.')
    print('')
    print('Controls:') 
    print('1) Movement: w-North, a-West, s-South, d-East')
    print('2) Weapon Choice: 1-Hershey Kisses, 2-Sour Straws,')
    print('                  3-Chocolate Bars, 4-Nerd Bombs')

    # create game object to host neighborhood and player objects
    g = Game()
    g.play()  # play the game
