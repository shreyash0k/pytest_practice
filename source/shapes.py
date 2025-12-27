import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        self.area = math.pi * self.radius ** 2
        return self.area

    def perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if not isinstance(other,Rectangle):
            return False
        
        return self.width == other.width and self.height == other.height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width * 2) + (self.height*2)
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    