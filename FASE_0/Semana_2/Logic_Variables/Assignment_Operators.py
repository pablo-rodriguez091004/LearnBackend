# ASSIGNMENT OPERATORS
# Store a value in a variable. Compound versions update the variable in place.

# Simple assignment (=)
x = 10

print("x = 10       ->", x)

# Add and assign (+=)  same as x = x + 5
x += 5
print("x += 5       ->", x)     # 15

# Subtract and assign (-=)
x -= 3
print("x -= 3       ->", x)     # 12

# Multiply and assign (*=)
x *= 2
print("x *= 2       ->", x)     # 24

# Divide and assign (/=) -> becomes a float
x /= 4
print("x /= 4       ->", x)     # 6.0

# Floor divide and assign (//=)
x //= 4
print("x //= 4      ->", x)     # 1.0

# Modulo and assign (%=)
y = 17
y %= 5
print("y = 17; y %= 5 ->", y)   # 2

# Exponent and assign (**=)
y **= 3
print("y **= 3      ->", y)     # 8

# Bitwise compound assignments (&=, |=, ^=, <<=, >>=)
z = 0b1100
z &= 0b1010
print("z &= 0b1010  ->", z)     # 8
z |= 0b0001
print("z |= 0b0001  ->", z)     # 9
z ^= 0b0011
print("z ^= 0b0011  ->", z)     # 10
z <<= 2
print("z <<= 2      ->", z)     # 40
z >>= 3
print("z >>= 3      ->", z)     # 5

# Multiple assignment
a = b = c = 0
print("a = b = c = 0 ->", a, b, c)

# Assign several values at once (tuple unpacking)
m, n = 1, 2
print("m, n = 1, 2  ->", m, n)

# Swap two variables
m, n = n, m
print("swap         ->", m, n)   # 2 1

# Walrus operator (:=) -> assign inside an expression
print("walrus       ->", (w := 7) * 2, "| w =", w)   # 14 | w = 7