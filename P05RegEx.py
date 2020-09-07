# Regex
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
# RegEx can be used to check if a string contains the specified search pattern.
#
# https://www.w3schools.com/python/python_regex.asp
#

import re

txt = "The rain in Spain is a tai pain and Hurts my brain"
x = re.search("^The.*ain$", txt)
print("<====1====>")
print(x)
print(x.string)

x = re.findall("\w+ai", txt)  #Anything starting with alpa/num and has an ai
print("<====2====>")
print(x)
print(f"Found: {len(x)}")
print(len(txt))

x = re.search(" ", txt)
print("<====3====>")
print(x)
print("The first white-space character is located in position:", x.start())

search_4 = " in "
x = re.search(search_4, txt)
print("<===4====>")
print(x)
print(f"The first [{search_4}] is located in position: {x.start()} -> End Position: {x.end()}")

code0 = 'txt = "The rain in Spain is a pain"'
code1 = 'search_4 = " in "\nx = re.search(search_4, txt)'
code2 = 'txt[x.end():][:re.search(" ",txt[x.end():]).start()]'
after_in_to_ = txt[x.end():][:re.search(" ", txt[x.end():]).start()]
print(f"\nLook for \" in \" in string \"{txt}\" and \nthen Look for first space after this, \n"
      f"and get whatever is there, Got: {after_in_to_}")

print(f"\nCode:\n{code0}\n{code1}\n{code2}")

# Take text that precedes search_4 in txt and put it into y
start1 = x.start()
y = txt[0:start1]

for i in txt.split(' '):
    print(i)

print("==========")

for i in y.split(' '):
    print(i)

print("===Split 2 =======")
print(txt.split(" ", 2))

txt = "The rain in Spain is awful, don't go to Spain when it rains"
x = re.sub("Spain", "Newark", txt)
print(x)

print("===sub : Replace =======")


txt = "The rain in Spain, stays mainly on the plain, don't fly to spain!"
x = re.sub("spain","Spain",txt)
x = re.sub("ain", "oon", x)

print(txt)
print(x)

print("===sub : Replace 3 =======")


txt = "The rain in Spain, stays mainly on the plain, don't fly to spain!"
x = re.sub("spain","Spain",txt)
x = re.sub("ain", "oon", x, 3)

print(txt)
print(x)

xx = "guru99,education is fun"
r1 = re.findall(r"^\w+",xx)


print(r1)
r1=r1[0]
print(r1)


list = ["guru99_123 get gappy", "guru99 give", "guru Selenium", "gum goo"]
print(list)
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element) # search for match,
    # start w g, \w+ w any alpha/num/_ till false then 1 non-alpha/num
    # then the next character must be a g, \w+ alpha/num/_ until False, if both are true, create

    if z:
        print(z.groups())
        print((z))
