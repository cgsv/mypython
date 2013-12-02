import math, operator, cv2
import numpy as np

class point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def distance(self, OtherPoint):
        return math.sqrt((self.x-OtherPoint.x)**2+(self.y-OtherPoint.y)**2)
    def midPoint(self, OtherPoint):
        return point(1.0/2*self.x+1.0/2*OtherPoint.x, 1.0/2*self.y+1.0/2*OtherPoint.y)
    def oneThirdPoint(self, OtherPoint):
        return point(2.0/3*self.x+1.0/3*OtherPoint.x, 2.0/3*self.y+1.0/3*OtherPoint.y)
    def twoThirdPoint(self, OtherPoint):
        return point(1.0/3*self.x+2.0/3*OtherPoint.x, 1.0/3*self.y+2.0/3*OtherPoint.y)
    def triPoint(self, OtherPoint):
        ang = math.atan((OtherPoint.y-self.y)/(OtherPoint.x-self.x))
        if OtherPoint.x < self.x:
            ang += math.pi
        ang1 = ang + math.pi/3.0
        dis = self.distance(OtherPoint)
        return point(self.x+dis*math.cos(ang1), self.y+dis*math.sin(ang1))
    def __repr__(self):
        return "point (%s, %s)" % (self.x, self.y, )

class line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def draw(self, img):
        cv2.line(img, (int(self.p1.x), int(self.p1.y)), (int(self.p2.x), int(self.p2.y)), (255, 0, 0), 1)
    def __repr__(self):
        return "Line (%s, %s)->(%s, %s)" % (self.p1.x, self.p1.y, self.p2.x, self.p2.y, )

class triangle:
    def __init__(self, p1, p2, p3):
        self.p1, self.p2, self.p3 = p1, p2, p3
        self.l1, self.l2, self.l3 = line(p1,p2), line(p2,p3), line(p3, p1)
    def draw(self, img):
        self.l1.draw(img)
        self.l2.draw(img)
        self.l3.draw(img)
    def midPoints(self):
        return self.p1.midPoint(self.p2),  self.p2.midPoint(self.p3),  self.p3.midPoint(self.p1)

def getOneFrac(line1):
    p1, p2 = line1.p1, line1.p2
    pa, pb = p1.oneThirdPoint(p2), p1.twoThirdPoint(p2)
    pc = pa.triPoint(pb)
    return [line(p1, pa), line(pa, pc), line(pc, pb), line(pb, p2)]

def flatmap(fun, li):
    return reduce(operator.add, map(fun, li))

def getOneTriFrac(tri):
    m1,m2,m3 = tri.midPoints()
    return [triangle(tri.p1, m1, m3), triangle(tri.p2, m2, m1), triangle(tri.p3, m3, m2)]

def getTriFracs(tris, times):
    if times == 0: return tris
    return flatmap(getOneTriFrac, getTriFracs(tris, times -1))

def getFracs(oriLines, times):
    if times == 0: return oriLines
    return flatmap(getOneFrac, getFracs(oriLines, times - 1))

def drawLines(lines, img):
    for l in lines:
        l.draw(img)

if __name__ == '__main__':
    #oriLine = line(point(980, 500), point(0, 500))
    p1 = point(200,180)
    p2 = point(800,180)
    p3 = p1.triPoint(p2)
    oLines = [line(p1,p3),line(p3,p2),line(p2,p1)]
    img = np.zeros((720, 1000, 3), np.uint8)
    i, step = 0, 1
    tri = triangle(p1,p2,p3)
    #drawLines(getTriFracs([tri],5), img)
    while 1:
        img[:] = 0
        #lines =  getFracs(oLines, i)
        lines = getTriFracs([tri], i)
        drawLines(lines, img)
        cv2.imshow('image', img)
        k = cv2.waitKey(1000)
        if k == 27:
            break
        i += step
        if i >= 6: step = -1
        elif i <= 0: step = 1
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
