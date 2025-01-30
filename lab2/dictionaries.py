# dictionaries
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# access to elements 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

# adding elements
car["color"] = "red"
# changing elements
car["color"] = "blue"

print(x) #after the change

#deleting elements
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# clear 
thisdict.clear()
print(thisdict)

#print both keys and values in dict
for x, y in thisdict.items():
  print(x, y)

# copy dicts 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# nested dicts

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

# Loop through the keys and values of all nested dictionaries:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

