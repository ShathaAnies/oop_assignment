from abc import ABC , abstractmethod
from itertools import cycle
class Shape (ABC) :
    @abstractmethod
    def area (self):
        pass

    @abstractmethod
    def perimeter (self):
        pass
class Sequare (Shape):
    def __init__(self , side):
        self.__side=side

    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return self.__side *4

class Rect(Shape):
    def __init__(self , lingth , width):
        self.__hingth= lingth
        self.__width =width

    def area(self):
        return self.__hingth * self.__width
    def perimeter(self):
        return 2* ( self.__hingth +self.__width)


class Triangle(Shape):
    def __init__(self , a , b ,c ,hight , base):
        self.__a= a
        self.__b =b
        self.__c =c
        self.__hight=hight
        self.__base=base

    def area(self):
        return  self.__a + self.__b + self.__c
    def perimeter(self):
        return 1/2 * self.__hight * self.__base
      


class Cycle(Shape):
    def __init__(self , diameter ):
        self.__diameter= diameter

    def area(self):
        return  2*  self.__diameter * 3.14
    def perimeter(self):
        return self.__diameter* self.__diameter * 3.14

sequare = Sequare (10)
rect=Rect( 4,6)
triangle = Triangle (5 ,8,5 ,9,4)
cycles = Cycle(8)

print (f"square area is: {sequare.area()} ==> square perimeter is: {sequare.perimeter()}")
print (f"square area is: {rect.area()} ==> square perimeter is: {rect.perimeter()}")
print (f"square area is: {triangle.area()} ==> square perimeter is: {triangle.perimeter()}")
print (f"square area is: {cycles.area()} ==> square perimeter is: {cycles.perimeter()}")