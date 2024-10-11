#create init that takes in the length and width, inherit to calculate area of quadrilateral
class Quadrilateral:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

class triangle(Quadrilateral):
    def area(self):
        return (self.length * self.width * 0.5)

# Polymorphism is changing a function to perform a different equation, as many times as you want.

quad1 = Quadrilateral(4, 2)
print(quad1.area())    
tri1 = triangle(4, 2)
print(tri1.area())