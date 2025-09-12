name = "Eric Idle"
password = "Eric*1934"

print("Welcome", name)
print("Your registration is complete")
print("Your temp password is", password)
print("*" * 10)

print("Welcome", name, '\n', "Your registration is complete", '\n', "Your temp password is: ", password)
print("*" * 10)
print("Welcome " + name, "Your registration is complete", "Your temp password is: " + password, sep='\n')
print("*" * 10)

print(f"""Welcome {name}
Your registration is complete
Your temp password is: {password}""")
