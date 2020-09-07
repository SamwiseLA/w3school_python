import json
# JSON
#
# JSON is a syntax for storing and exchanging data.
#
# JSON is text, written with JavaScript object notation.
#

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

print("Jason Data")
print(x)
print("Python: JASON data converted to Python Dictionary")
print(y)

# Convert Python to JASON
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print("")

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(x)
print(y)

# More Examples

print("")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Billy","Ann"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(x)
print(y)


print("\n<--- Indents --->")
# Logical Indents for readability

# use four indents to make it easier to read the result: Looks for []{}(), and m oves to next line and indents
print(json.dumps(x, indent=4))

print("\n<--- Indents AND uses specifide Separators --->")
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print("\n<--- Indents with Sort by first node --->")
# Logical Indents for readability sorted
print(json.dumps(x, indent=4, sort_keys=True))
