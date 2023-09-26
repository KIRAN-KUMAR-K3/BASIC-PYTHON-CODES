import math
class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of Rectangle:",area)
class Circle(Rectangle):
    def cir_area(self, radi):
        area = math.pi*radi*radi
        print("Area of Circle:", area)
class Triangle(Circle):
    def tri_area(self, length,breadth):
        area = 0.5*length*breadth
        print("Area of Triangle:", area)
obj=Triangle()
obj.rec_area(10,20)
obj.cir_area(2)
obj.tri_area(12,25)