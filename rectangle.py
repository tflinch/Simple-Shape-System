class Shape():
    def __init__(self,color):
        self.color = color

    def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
    def __str__(self):
        return 'Shape color {} '.format(
            self.color,)
    
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * self.height +self.width
    
    def __str__(self):
        return 'Rectangle height {} Rectangle width {} Shape color{}'.format(self.height, self.width, self.color)
    
new_shape = Shape('black')
new_rectangle = Rectangle('yellow',45,25)

print(str(new_rectangle))