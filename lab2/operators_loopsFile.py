# operators how they work
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#operators using while loop
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# for loop 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# using ranges 
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)