#!usr/bin/env python3

from observer_pattern.observer import Observer
from observer_pattern.observable import Observable


class House(Observer, Observable):
    def update_observer(self):
        print('Monster updated!')

    def update_observable(self):
        print('Population updated!')
