import matplotlib.pyplot as pl
from matplotlib import collections
from math import pi, sin, cos
from numpy import amax,amin,array

class L_System(object):
    def __init__(self, rule):
        info = rule['S']
        for i in range(rule['iter']):
            ninfo = []
            for c in info:
                if c in rule:
                    ninfo.append(rule[c])
                else:
                    ninfo.append(c)
            info = ''.join(ninfo)
        self.rule = rule
        self.info = info

    def get_lines(self):
        d = self.rule['direct']
        a = self.rule['angle']
        p = (0.0,0.0)
        l = 1.0
        lines, stack = [], []
        for c in self.info:
            if c == 'F':
                r = d * pi / 180
                t = p[0] + l*cos(r), p[1] + l*sin(r)
                lines.append([[p[0],p[1]],[t[0],t[1]]])
                p = t
            elif c == '+':
                d += a
            elif c == '-':
                d -= a
            elif c == '[':
                stack.append((p,d))
            elif c == ']':
                p,d = stack[-1]
                del stack[-1]
        return lines

rule = {"X": "F-[[X]+X]+F[+FX]-X",
        "F": "FF",        
        "S": "X",
        "direct": -45,
        "angle": 25,
        "iter": 2,
        "title": "Plant"}

lines = L_System(rule).get_lines()
xmin,xmax =  amin(array(lines)[:,:,0]),amax(array(lines)[:,:,0])
ymin,ymax =  amin(array(lines)[:,:,1]),amax(array(lines)[:,:,1])
fig = pl.figure()
ax = fig.add_subplot(111)
ax.set_xlim((xmin,xmax))
ax.set_ylim((ymin,ymax))
linecollections = collections.LineCollection(lines)
ax.add_collection(linecollections)
pl.show()

