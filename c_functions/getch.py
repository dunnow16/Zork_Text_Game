#!usr/bin/env python3


class _Getch:
    """
    All code in this file from:
    http://code.activestate.com/recipes/134892/
    3/18/2018
    Gets a single character from standard input. Does not echo to the
    screen.
    """
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    """Works on EOS Centos, Linux system."""
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    """
    This code doesn't seem to work on Windows 10.
    """
    # def __init__(self):
    #     import msvcrt
    #
    # def __call__(self):
    #     import msvcrt
    #     return msvcrt.getch()

    def __call__(self):  # for win10 testing
        ch = input('')
        return ch
