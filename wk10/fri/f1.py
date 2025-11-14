
filename = "wk10/fri/name.txt"

data = open(filename)  # filename[, mode] 
# r => read (default)
# a => append => write to end of file
# w => write => delete current contents of file, write data to fresh file

content = data.read()  # read(), readline(), readlines()
if len(content) == 0:
    name = input("What is your name? ")
    data.close()
    data = open(filename, "w")
    data.write(name)
else:
    name = content.strip()

print("Hello", name)
