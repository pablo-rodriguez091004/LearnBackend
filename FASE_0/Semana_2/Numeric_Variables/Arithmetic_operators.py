# ARITHMETIC OPERATORS
# Used for basic math with numbers.

a = 17
b = 5

# Addition (+)
print("17 + 5  =", a + b)       # 22

# Subtraction (-)
print("17 - 5  =", a - b)       # 12

# Multiplication (*)
print("17 * 5  =", a * b)       # 85

# Division (/) -> always returns a float
print("17 / 5  =", a / b)       # 3.4

# Floor division (//) -> division rounded down to an integer
print("17 // 5 =", a // b)      # 3

# Modulo (%) -> remainder of the division
print("17 % 5  =", a % b)       # 2

# Exponent (**) -> power
print("17 ** 5 =", a ** b)      # 1419857

# Negation (-) and positive (+) on a single value
print("-a =", -a)               # -17
print("+a =", +a)               # 17

# Works with floats too
print("7.5 + 2.5 =", 7.5 + 2.5)     # 10.0
print("7.5 // 2  =", 7.5 // 2)      # 3.0

# Operator precedence: ** first, then * / // %, then + -
print("2 + 3 * 4    =", 2 + 3 * 4)       # 14
print("(2 + 3) * 4  =", (2 + 3) * 4)     # 20
print("2 ** 3 ** 2  =", 2 ** 3 ** 2)     # 512 (right to left)