class Point:
    def __init__(self,x,y):
        self.x,self.y = x,y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(2,3)
p2 = Point(4,1)

print(p1 + p2)

