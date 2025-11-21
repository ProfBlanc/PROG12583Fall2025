class Person:
    def __init__(self, name="Person", height=100, weight=50):
        self.set_name(name)
        self.set_height(height)
        self.set_weight(weight)
    
    def test(self): return "I love tests!"
    def eat(self, what):
        return f"{self._name} is eating {what}"
    def sleep(self, duration, time_unit):
        return f"{self._name} is sleeping for {duration} {time_unit}"
    def __str__(self): return f"Name:{self._name}, Height: {self._height}, Weight:{self._weight}"
    
    def set_name(self, name):
        self._name = name if isinstance(name, str) and len(name) >= 3 else "Default"
    def set_height(self, height):
        self._height = height if isinstance(height, int) and height >=30 else 30
    def set_weight(self, weight):
        self._weight = weight if isinstance(weight, int) and weight >=40 else 40
        
    def get_name(self): return self._name
    def get_height(self): return self._height
    def get_weight(self): return self._weight
    
p1 = Person("Ben", 105, 55)
print(p1)

# p1.name = True
# p1.height=1
# p1.weight = -1

print(p1.get_name())