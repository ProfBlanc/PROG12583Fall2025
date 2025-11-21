class Person:
    def __init__(self, name="Person", height=100, weight=50):
        self.name = name if isinstance(name, str) and len(name) >= 3 else "Default"
        self.height = height if isinstance(height, int) and height >=30 else 30
        self.weight = weight if isinstance(weight, int) and weight >=40 else 40
    
    def test(self): return "I love tests!"
    def eat(self, what):
        return f"{self.name} is eating {what}"
    def sleep(self, duration, time_unit):
        return f"{self.name} is sleeping for {duration} {time_unit}"


p1 = Person("Ben", 105, 55)
print(p1.name, p1.height, p1.weight)

print(p1.eat(what="food"))
print(p1.eat("chips"))
print(p1.test())
print(p1.sleep(30, "minutes"))