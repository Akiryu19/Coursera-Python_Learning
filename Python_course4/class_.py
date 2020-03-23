class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

p = Point()
q = Point()

print(p is q)

class NumberSet():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
t = NumberSet(1,10)
print(t)


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


p = Point(7,6)
print(p.getX())
print(p.getY())


class Animal:
    def __init__(self,arms,legs):
        self.arms = arms
        self.legs = legs
    def limbs(self):
        return (self.arms + self.legs)
spider = Animal(4,4)
spidlimbs = spider.limbs()
print(spidlimbs)
