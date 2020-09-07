# Using Modules

import mymodule as mm

s_name = "?"

while s_name != "":
    s_name = input("Name: ")
    if s_name != "":
        mm.greeting(s_name)

print(mm.person1)

p1_age = mm.person1["age"]
print(p1_age)

# Built in Modules
print("<===== Built in Modules =====>")

import platform

x = platform.system()
print(x)
x = platform.node()
print(x)
x = platform.release()
print(x)
x = platform.version()
print(x)
x = platform.machine()
print(x)

# Using the dir() function
print("\n<===== dir() function =====>\n")

y = dir(platform)
for x in y:
    print(x)

print("\n<---->\n")

y = dir(mm)
for x in y:
    print(x)

# Import only a p[art of a module
print("\n<----- Import ONLY the Person1 part of MyModule\n")

from mymodule import person1 as locp1

x = locp1["country"]
print(x)




