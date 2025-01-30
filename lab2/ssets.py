# set 
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3, 5}
set3 = {True, False, False}
print(set2, set3)

# elements in set 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# checking if it is in 
print("banana" in thisset)

#adding elements
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# updating sets
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

#removing elements
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#joining sets
"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# union can be written as a |
set3 = set1.union(set2)
print(set3)

# intersection can use the & operator instead of the intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# difference() can use the - operator instead of the difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# symmetric_difference() can use the ^ operator instead of the symmetric_difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)