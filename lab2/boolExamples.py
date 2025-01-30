print(10 > 9)
print(10 == 9)
print(10 < 9)

# if else operations
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# bool function

print(bool("Hello"))
print(bool(15))

# when bool prints False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# function prints boolean outputs
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# function checks if this is number
x = 200
print(isinstance(x, int))