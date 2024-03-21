class Circle:

    def __init__(self, diameter: float):
        self.diameter = diameter
        self.__pi = 3.14

    def calculate_circumference(self):
        return self.diameter * self.__pi

    def calculate_area(self):
        return self.__pi * ((self.diameter / 2) ** 2)

    def calculate_area_of_sector(self, angle: float):
        return (angle / 360) * (self.__pi * ((self.diameter / 2) ** 2))


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
