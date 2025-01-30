# List's basic operations
list1 = ["abc", 34, True, 40, "male"]
print(len(list1))
print(type(list1))

# access to elements
print(list1[1], list1[-2], list1[-4:-1])

# inserting, changing elements in list
newOne = [1, 3, 4, 3]
newOne[1:3] = [7, 8]
newOne[1:2] = [2, 5]
newOne[-1] = 9
print(newOne)

# inserting using function
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#adding elements using built-in functions
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist.append("pean")
print(thislist)

# removing elements
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # first occurance of banana
print(thislist)

thislist.pop(0)
thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

thislist.clear()
print(thislist)

# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# using indexes
for i in range(len(thislist)):
    print(thislist[i]) 

# List comprehensions
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits] 
print(newlist)
newlist.clear()
# number which are less than 5
newlist = [x for x in range(10) if x < 5]
print(newlist)

# sorting list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry", "peanut"]
thislist.sort(key = str.lower)
print(thislist)

#3 ways to copy list
# 1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# 2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# 3
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Joining two lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# another method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# function I did not mention
b = [1,2, 3, 4]
b.reverse()
print(b)

ind = b.index(3)
print(ind)

