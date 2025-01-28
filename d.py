import math
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"Выведите точки:({self.x},{self.y})")
    def move(self,new_x,new_y):
        self.x = new_x
        self.y = new_y 
        print(f"Выведите другие точки:({self.x},{self.y})")
    
    def dist(self,other):
        dista = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        print(f"distance: {dista:.3f}")

x1 = float(input("Выедите х1:"))
y1 = float(input("Выведите y1:"))
point1 = point(x1,y1)

x2 = float(input("Выведите x2:"))
y2 = float(input("Выведите y2:"))
point2 = point(x2,y2)

print("\nПервая точка:")
point1.show()

print("\nВторая точка:")
point2.show()

new_x = float(input("\nКоординаты для новых х1:"))
new_y = float(input("\nКоординаты для новых у1:"))
point1.move(new_x,new_y)

print("\nРасстояние между точками:")
point1.dist(point2)

    
