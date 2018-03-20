#!usr/bin/env python3

from abc import ABCMeta, abstractmethod


class Observer(object):
    __metaclass__ = ABCMeta
  
    @abstractmethod
    def update_observer(self):
        pass
