#!/usr/bin/env python
"""
An attempt at an othello game.
"""

import sys, random

from PyQt4 import QtCore, QtGui

class space:
    def __init__(self,x=None, y=None):
        self.value = None
        self.x_loc = x
        self.y_loc = y
    def __str__(self):
        if self.value:
            return '| %s ' % self.value
        else:
            return '|   '
    def set_value(self, v):
        if v in ['R','B',None]:
            self.value = v
        else:
            raise ValueError
    def flip(self):
        if self.value =='R':
            self.value =='B'
        elif self.value == 'B':
            self.value == 'R'





class board:
    def __init__(self):
        self.spaces = {}
        for x in range(8):
            for y in range(8):
                self.spaces[str(x)+':'+str(y)] = space(x,y)

    def setup(self):
        self.spaces[str(3)+':'+str(3)].value = 'R'
        self.spaces[str(4)+':'+str(4)].value = 'R'
        self.spaces[str(3)+':'+str(4)].value = 'B'
        self.spaces[str(4)+':'+str(3)].value = 'B'

    def __str__(self):
        result = '   '
        result += ' ' *5 + 'Othello\n'
        result += '   ' + '____' *8 +'\n'
        result += '   ' + '__%s_'*8 % tuple([chr(i) for i in range(65, 73)]) +'\n'
        for x in range(8):
            result += '%s  ' % (x+1)
            for y in range(8):
                result += str(self.spaces[str(x)+':'+str(y)])
            result += '\n'
        return result



def main():
    a = board()
    print(a)
    a.setup()
    print(a)





if __name__=='__main__':
    main()