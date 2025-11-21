"""
All things on earth have components
    attributes: how it looks/how to describe
    actions: how it behaves/what it can do

example
Person
    attributes
        has a name
        has a height
        has a weight
    actions
        studies
        eats
        sleeps

In a class, all attributes are stored in 
a special method called constructor
definition of this method is 
__init__()

"""
class Person:
    name = "Person"
    weight = 50
    height = 100
        """
    def __init__(self):
        self.name = "Person"
        self.height = 100
        self.weight = 50
    """

    
    
p1 = Person()
print(p1.name, p1.weight, p1.height)
p1.name = "Changed"
p1.weight = 60
p1.height = 110
print(p1.name, p1.weight, p1.height)

p2 = Person()
print(p2.name, p2.weight, p2.height)
