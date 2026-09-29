# LOGICAL OPERATORS
# Combine or invert conditions (True / False values).

age = 25
has_id = True
is_student = False

# and -> True only if BOTH sides are True
print("age >= 18 and has_id       :", age >= 18 and has_id)         # True
print("age >= 18 and is_student   :", age >= 18 and is_student)     # False

# or -> True if AT LEAST ONE side is True
print("is_student or has_id       :", is_student or has_id)         # True
print("is_student or age < 18     :", is_student or age < 18)       # False

# not -> inverts the value
print("not is_student             :", not is_student)               # True
print("not has_id                 :", not has_id)                   # False

# Combining all three (not first, then and, then or)
print("not is_student and has_id or age < 18 :",
      not is_student and has_id or age < 18)                        # True

# Use parentheses to make the order clear
print("(is_student or has_id) and age > 30   :",
      (is_student or has_id) and age > 30)                          # False

# Short-circuit: Python stops as soon as the result is known
print("False and (1 / 0)  :", False and (1 / 0))    # False, 1/0 never runs
print("True or (1 / 0)    :", True or (1 / 0))      # True, 1/0 never runs

# and / or return one of the values, not always True / False
print("'hello' and 'world' :", "hello" and "world")   # world
print("'' or 'default'     :", "" or "default")       # default
print("0 or 5              :", 0 or 5)                # 5
print("3 and 0             :", 3 and 0)               # 0

# Falsy values: False, 0, 0.0, "", [], {}, (), set(), None
print("not 0    :", not 0)         # True
print("not ''   :", not "")        # True
print("not []   :", not [])        # True
print("not None :", not None)      # True
print("not 'a'  :", not "a")       # False