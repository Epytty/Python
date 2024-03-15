# -*- coding: utf-8 -*-
"""

  дешифратор "2 в 4"

"""
from logelement import *

"""---------------------------------------------
  Класс TDecoder - дешифратор "2 в 4"
---------------------------------------------"""
class TDecoder(TLog2In):
    def __init__(self):
        self.In1 = False
        self.In2 = False
        self._res = False

    def calc(self):
        if not self.In1 and not self.In2:
            self._res = True
        elif not self.In1 and self.In2:
            self._res = False
        elif self.In1 and not self.In2:
            self._res = False
        elif self.In1 and self.In2:
            self._res = False

    def Output(self, no):
        if no == 1:
            return int(not self._res)
        elif no == 2:
            return int(self._res and not self.In1 and self.In2)
        elif no == 3:
            return int(self._res and not self.In1 and not self.In2)
        else:
            return int(self._res and self.In1 and not self.In2)

#---------------------------------------------------
# Основная программа
#---------------------------------------------------

decoder = TDecoder()

print(' C1 C0 | X3 X2 X1 X0');
print('---------------------');

for C1 in range(2):
    for C0 in range(2):
        decoder.In1 = bool(C0)
        decoder.In2 = bool(C1)
        print('  ', int(C1), '  ', int(C0),
              ' |  ', int(decoder.Output(3)),
              '  ', int(decoder.Output(2)),
              '  ', int(decoder.Output(1)),
              '  ', int(decoder.Output(0)), sep="");