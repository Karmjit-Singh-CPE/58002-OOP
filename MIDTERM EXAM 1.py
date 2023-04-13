class Circle():
    def area(self, radius):
        print("Area of the circle is:", 3.142 * radius * radius)

    def perimeter(self, radius):
        print("Perimeter of the circle is:", 2 * 3.14 * radius)

c = Circle()
radius = float(input("Enter the radius of the circle: "))
c.area(radius)
c.perimeter(radius)
