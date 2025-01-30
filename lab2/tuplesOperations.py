# this is tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# printing tuples using indexes
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
print(thistuple[2:])
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# adding items to tuple 2 ways
# 1
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
# 2
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# packing tuples will create topic list and store all elements except 1 and last
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#looping inside tuple
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# joining tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# tuple functions
tuple1 = ("a", "b" , "c", "a")
print(tuple1.count("a"))
print(tuple1.index("c"))




