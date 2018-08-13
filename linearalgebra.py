
###defining Vector####
import math
class Vector(object):
    def __init__(self,cordinates):
        try:
            if not cordinates:
                raise ValueError

            self.cordinates = tuple(cordinates)
            self.dimencsion = len(cordinates)


        except ValueError:
            raise ValueError('The cordinates are empty')

        except TypeError:
            raise TypeError('The value are iterable')
    def sum(self,v):
        new_cord=[x+y for x,y in zip(self.cordinates, v.cordinates)]
        return Vector(new_cord)

    def sub(self,v):
        new_cord=[x-y for x,y in zip(self.cordinates,v.cordinates)]
        return  Vector(new_cord)

    def time_scalar(self,c):
        new_cord=[c*x for x in self.cordinates]
        return Vector(new_cord)
    
    def magnitude(self):
        new_cord=0
        new_cord=[ x**2 for x in self.cordinates]
        return math.sqrt(sum(new_cord))

    def dot(self,v):
        return sum([x*y for x,y in zip(self.cordinates,v.cordinates)])

    def  norm(self):
        return self.time_scalar(1/self.magnitude())
        
    def __str__(self):
        return 'Vector:{}'.format(self.cordinates)

    def __eq__(self,v):
        return self.cordinates == v.cordinates

    def angle(self,v):
        u1=self.norm()
        u2=v.norm()
        print (u1)
        print (u2)
        



v=Vector([7.887,4.138])
w=Vector([-8.802,6.776])
print(v.angle(w))




