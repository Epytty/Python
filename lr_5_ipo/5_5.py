'B * (C mod2 (not A))'

import logelement_1_for_st as logelement
class TLogElement_AND(logelement.TLogElement):
    def calc(self):
        self._res = self._TLogElement__in1 and self._TLogElement__in2
class TMod2(logelement.TLogElement):
    def calc(self):
        if (self._TLogElement__in1 and not self._TLogElement__in2) or (not self._TLogElement__in1 and self._TLogElement__in2):
            self._res = True
        else:
            self._res = False
class TLogElement_NOT(logelement.TLogElement):
    def calc(self):
        self._res = not self._TLogElement__in1
class TLogElement_OR(logelement.TLogElement):
    def calc(self):
        self._res = self._TLogElement__in1 or self._TLogElement__in2
A = [False, True]
B = [False, True]
C = [False, True]
print("A B C | B * (C mod2 (not A))")
print("------+-------------------")
for a in A:
    for b in B:
        for c in C:
            elA = TMod2()
            elB = TLogElement_NOT()
            elC = TLogElement_AND()
            elD = TMod2()
            elE = TLogElement_AND()
            elF = TMod2()
            elA.In1 = c
            elA.In2 = elB.Res
            elB.In1 = a
            elC.In1 = b
            elC.In2 = elA.Res
            elD.In1 = b
            elD.In2 = elB.Res
            elE.In1 = elC.Res
            elE.In2 = elD.Res
            elF.In1 = b
            elF.In2 = elE.Res
            print(" ", int(a), int(b), int(c), "|", int(elF.Res))