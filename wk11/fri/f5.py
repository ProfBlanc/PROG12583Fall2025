class Person:
    def __init__(self, name="Person", height=100, weight=50):
        self.name = name if isinstance(name, str) and len(name) >= 3 else "Default"
        self.height = height if isinstance(height, int) and height >=30 else 30
        self.weight = weight if isinstance(weight, int) and weight >=40 else 40


# p1 = Person(True, 1.1, "boo")
p1 = Person("Ben", -20, 10)
print(p1.name, p1.height, p1.weight)


