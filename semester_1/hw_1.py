class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Rect:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __str__(self):
        return f"Rect (top left: {self.top_left}, bottom right: {self.bottom_right})"

    def sides(self):
        width = abs(self.bottom_right.x - self.top_left.x)
        height = abs(self.bottom_right.y - self.top_left.y)
        return width, height

    def perim(self):
        width, height = self.sides()
        return 2 * (width + height)


# Пример использования
if __name__ == "__main__":
    # Создаем объекты класса Point
    point1 = Point(1, 2)
    point2 = Point(4, 6)

    # Создаем объект класса Rect
    rectangle = Rect(point1, point2)

    # Выводим информацию о точках и прямоугольнике
    print("Point 1:", point1)
    print("Point 2:", point2)
    print("Rectangle:", rectangle)

    # Вызываем методы для прямоугольника
    print("Sides of the rectangle:", rectangle.sides())
    print("Perimeter of the rectangle:", rectangle.perim())
