# MEMBERSHIP OPERATORS
# Check if a value is (or is not) inside a sequence or collection.

# in      -> True if the value is found
# not in  -> True if the value is NOT found

# In a list
numbers = [1, 2, 3, 4, 5]
print("3 in numbers     :", 3 in numbers)        # True
print("9 in numbers     :", 9 in numbers)        # False
print("9 not in numbers :", 9 not in numbers)    # True

# In a string (checks for substrings)
text = "Hello, Python"
print("'Python' in text :", "Python" in text)    # True
print("'Java' in text   :", "Java" in text)      # False
print("'h' in text      :", "h" in text)         # False (case sensitive)

# In a tuple
colors = ("red", "green", "blue")
print("'green' in colors :", "green" in colors)  # True

# In a set (very fast lookup)
unique_ids = {101, 102, 103}
print("102 in unique_ids :", 102 in unique_ids)  # True

# In a dict -> checks the KEYS
person = {"name": "Pablo", "age": 20}
print("'name' in person     :", "name" in person)         # True
print("'Pablo' in person    :", "Pablo" in person)        # False (it is a value)
print("'Pablo' in values    :", "Pablo" in person.values())   # True

# In a range
print("7 in range(0, 10)  :", 7 in range(0, 10))     # True
print("10 in range(0, 10) :", 10 in range(0, 10))    # False (10 is excluded)

# Using it inside an if
fruit = "apple"
if fruit in ["apple", "banana", "orange"]:
    print(fruit, "is in the fruit list")

# Using it in a loop
for letter in "abc":
    print("letter:", letter)