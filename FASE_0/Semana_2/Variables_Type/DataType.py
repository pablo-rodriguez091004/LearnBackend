# Text Type: str
text = "Hello, Python"
print(text, type(text),)

# Numeric Types: int, float, complex
integer = 42
decimal = 3.14
complex_number = 2 + 3j
print(integer, type(integer))
print(decimal, type(decimal))
print(complex_number, type(complex_number))

# Sequence Types: list, tuple, range
my_list = [1, 2, 3, "four"]
my_tuple = (10, 20, 30)
my_range = range(0, 10, 2)
print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_range, type(my_range))

# Mapping Type: dict
person = {"name": "Pablo", "age": 20}
print(person, type(person))

# Set Types: set, frozenset
my_set = {1, 2, 3, 3, 2}
my_frozenset = frozenset([1, 2, 3, 3])
print(my_set, type(my_set))
print(my_frozenset, type(my_frozenset))

# Boolean Type: bool
is_true = True
is_false = False
print(is_true, type(is_true))
print(is_false, type(is_false))

# Binary Types: bytes, bytearray, memoryview
my_bytes = b"Python"
my_bytearray = bytearray(b"Python")
my_memoryview = memoryview(my_bytes)
print(my_bytes, type(my_bytes))
print(my_bytearray, type(my_bytearray))
print(my_memoryview, type(my_memoryview))

# None Type: NoneType
nothing = None
print(nothing, type(nothing))