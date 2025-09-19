"""
AND
OR
NOT
    logical operators
        combine relational operators

"""
age = 20
height = 150

print(age >= 20 and height < 200)
print(age == 10 or age == 20 or age == 30)
print(height > 200 or height % 50 == 0)

print(not age == 20)
print(age != 20)

answer = input("Enter your password: ")
if answer == "password" or answer == "password1" or answer == "12345678":
    print("Password is too common")
else:
    print("Password is good")

print("*" * 20)
if not answer == "password" and not answer == "password1" and not answer == "12345678":
    print("Password is good")
