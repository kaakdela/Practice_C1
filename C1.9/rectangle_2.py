from rectangle import Rectangle, Square, Circle

# далее создаем два прямоугольника

rect1 = Rectangle(3,4)
rect2 = Rectangle(12,5)
#вывод площадки двух наших прямоугольников

print(rect1.get_area())
print(rect2.get_area())

square1 = Square(5)
square2 = Square(10)

print(square1.get_area_square(),
      square2.get_area_square())

circle1 = Circle(10)
print(circle1.get_area_circle())

fugures = [rect1, rect2, square1, square2, circle1]
for figure in fugures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())
