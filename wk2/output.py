"""
print() is an amazing method
    Used to output data to screen
    data = literal value or variable value
    screen = console = terminal = black box that states file path and output

You can output multiple values or single values
    alternate between literal values and variables    

print can outside an unlimited amount of arguments

print has two important special arguments
    sep 
        how to seperate each argument
    end
        the ending character

"""
print("Hello World")

name = "Ben"    

print("Hi, my name is", name)  # alternating b/w litteral and variable values

print("Hi, my  name is " + name)  # concatenation

print("The prof's name is", name, "He teaches us" + "python")

print("It is", 15, "degrees Celsius outside today.")
print("*" * 15)
print("The prof's name is", name, sep="------")
temp = 15
print("Prof name is", name, ".", "Temp outside is", temp, sep="###")

print("*" * 10)  # repeat characters
print("abc " * 5)
print("Hello World! " * 10)
print("*" * 15)
print("Is this a fun class", end="? ")
print("Yes it is!")

print("*" * 15)

# what is the output of the following print statement?
print("Today is", "friday, " * 3, "!", "The best day of the week", ", right", sep="_", end="?!")

# Today is_friday, friday, friday, _!_The best day of the week_, right?!
print("*" * 10)
print("Hi, There!", name, sep="yadda, yadda, yadda")
