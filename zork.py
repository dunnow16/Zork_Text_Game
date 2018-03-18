#!usr/bin/env python3

from observer_pattern.observer import Observer
from observer_pattern.observable import Observable

class House(Observer):
    def update(self):
        print('Monster updated!')
    
class Monster(Observable):
    pass

if __name__ == "__main__":
    h = House()
    vampire = Monster()
    mummy = Monster()
    
    vampire.add_observer(h)
    mummy.add_observer(h)
    
    vampire.update()
    mummy.update()