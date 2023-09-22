#stat_calc.py 

import math

class Stat_Calc():

    def __init__(self, hp, atk, dfn, sp_atk, sp_dfn, spd):

        self._hp = int(hp) 

        self._atk = int(atk)

        self._dfn = int(dfn)

        self._sp_atk = int(sp_atk)

        self._sp_dfn = int(sp_dfn)

        self._spd = int(spd)

    def hp_calc(self, hp_iv, hp_ev, lvl):

        hp = ((((2 * self._hp) + hp_iv + (hp_ev//4)) * lvl)//100) + lvl + 10

        return hp

    def _stat_calc(self, base, iv, ev, lvl, nature):

        temp = (((((2 * base) + iv + (ev//4)) * lvl)//100) + 5) * nature

        stat = math.floor(temp)

        return stat

    def decide_stat(self, stat_dfn, iv, ev, lvl, nature):

        if stat_dfn.lower() == 'attack':

            return self._stat_calc(self._atk, iv, ev, lvl, nature)

        elif stat_dfn.lower() == 'defense':

            return self._stat_calc(self._dfn, iv, ev, lvl, nature)

        elif stat_dfn.lower() == 'special defense':

            return self._stat_calc(self._sp_dfn, iv, ev, lvl, nature)

        elif stat_dfn.lower() == 'special attack':

            return self._stat_calc(self._sp_atk, iv, ev, lvl, nature)

        elif stat_dfn.lower() == 'speed':

            return self._stat_calc(self._spd, iv, ev, lvl, nature)

        else:

            raise ValueError