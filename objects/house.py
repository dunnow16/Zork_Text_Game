#!usr/bin/env python3

from observer_pattern.observer import Observer
from observer_pattern.observable import Observable

class House(Observer, Observable):
    def updateObserver(self):
        print('Monster updated!')