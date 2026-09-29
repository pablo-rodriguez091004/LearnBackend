# COMPARISON (RELATIONAL) OPERATORS
# Compare two values. The result is always True or False.

a = 10
b = 20

# Equal to (==)
print("10 == 20 :", a == b)     # False

# Not equal to (!=)
print("10 != 20 :", a != b)     # True

# Greater than (>)
print("10 > 20  :", a > b)      # False

# Less than (<)
print("10 < 20  :", a < b)      # True

# Greater than or equal to (>=)
print("10 >= 10 :", a >= 10)    # True

# Less than or equal to (<=)
print("20 <= 10 :", b <= a)     # False

# Chained comparison
x = 15
print("10 < 15 < 20 :", a < x < b)    # True
print("10 < 15 < 12 :", a < x < 12)   # False

# Comparing different types
print("5 == 5.0   :", 5 == 5.0)        # True (same value)
print("'a' < 'b'  :", "a" < "b")       # True (alphabetical order)
print("'apple' == 'apple' :", "apple" == "apple")   # True

# Comparing lists
print("[1, 2] == [1, 2] :", [1, 2] == [1, 2])   # True
print("[1, 2] < [1, 3]  :", [1, 2] < [1, 3])    # True (compares item by item)