# IDENTITY OPERATORS
# Check if two names point to the SAME object in memory (not just equal values).

# is      -> True if both are the same object
# is not  -> True if they are different objects

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

# Same values, different objects
print("list_a == list_b     :", list_a == list_b)   # True  (same values)
print("list_a is list_b     :", list_a is list_b)   # False (different objects)

# list_c points to the same object as list_a
print("list_a is list_c     :", list_a is list_c)   # True
print("list_a is not list_b :", list_a is not list_b)   # True

# Changing one changes the other when they are the same object
list_c.append(4)
print("list_a after append  :", list_a)              # [1, 2, 3, 4]

# id() shows the memory identity of an object
print("id(list_a) == id(list_c) :", id(list_a) == id(list_c))   # True

# Most common use: comparing with None
value = None
print("value is None     :", value is None)          # True
print("value is not None :", value is not None)      # False

# Same for True / False (they are single objects)
flag = True
print("flag is True :", flag is True)                # True

# Small integers and short strings can be reused by Python,
# so use == to compare values and is only for None / True / False / same object
n1 = 5
n2 = 5
print("n1 is n2 :", n1 is n2)                        # True (small ints are cached)
print("n1 == n2 :", n1 == n2)                        # True