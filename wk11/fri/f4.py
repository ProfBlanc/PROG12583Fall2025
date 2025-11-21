class Person:
    def __init__(self, name="Person", height=100, weight=50):
        self.name = name
        self.height = height
        self.weight = weight

    
    
p1 = Person("Changed", 110, 60)
print(p1.name, p1.weight, p1.height)

p2 = Person()
print(p2.name, p2.weight, p1.height)

