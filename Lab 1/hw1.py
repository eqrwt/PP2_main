#2nd problem
import sys

print(sys.version)

# here 1st assignment  
print("Hello world")

#here example using variable and input from terminal
n = int(input())

#here another example of using if
if n > 2:
    print("No there other people here")
if n == 2:
    print("Just the two of us")


#here good example of using global and other things in working with variables
x = "awesome"

def myfunc():
  x = "fantastic"
myfunc()
print("Python is " + x)

# here adding global keyword to show how we can change x

x = "awesome"

def myfunc():
  global x  
  x = "fantastic"
myfunc()
print("Python is " + x)

# identyfing variables type here how

haski = set((1, 2, 2, 3))
print(type(haski))


# playing with type of numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

def wanna_work_with_function_starting_from_this():
    x = str("s1") # x will be 's1'
    y = str(2)    # y will be '2'
    z = str(3.0)  # z will be '3.0' 
    print(y)
    y = int(y)
    print(y)

def working_with_strings():
    s = 'Lollipop lolilolilolilolipop'
    print(s[-1] + s[0])
    print(s[4:3], s[-1:0:-1])
    print(f'I remembered son from {s[0:4]} good one I do not know if it is wrong we will seee')

