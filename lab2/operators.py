# Addition and subtraction, multiplication, division, floor division, and modulus
x = 5
print((x*3+x*8-14) / (x % 2) * (x // 3))

# Bitwise AND Bitwise XOR Bitwise OR Bitwise NOT
x = 7  # bit - 0111
y = 3  # bit - 0011
print(x & y) # result bit - 0011 ans: 3

print(7 | 3) # result bit - 0111 ans: 7

print(7 ^ 3) # result bit - 0100 ans: 4

print(~x) # result bit - 0111 ans: 8

# Comparisons, identity, and membership operators not Logical NOT and AND or OR
print(3 == 2)
print(3 != 2)
print(3 >= 2)
print(3 > 4 or 5 <= 5)
x = 5
print(x < 10 and x > 2)
print((x is not 5) or (x is 5))

# Bitwise left and right shifts
x = 12 # bit 1100 
print(x << 2) # 110000 ans: 48
print(x >> 2) # 011 ans: 3





