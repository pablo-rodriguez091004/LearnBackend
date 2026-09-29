# ---------- int ----------
decimal_int = 42
negative_int = -7
big_int = 10 ** 30            # no size limit in Python
binary_int = 0b1010           # binary -> 10
octal_int = 0o17              # octal  -> 15
hex_int = 0xFF                # hex    -> 255
readable_int = 1_000_000      # underscores for readability
print(decimal_int, type(decimal_int))
print(negative_int, big_int)
print(binary_int, octal_int, hex_int)
print(readable_int)

# ---------- float ----------
simple_float = 3.14
scientific_float = 1.5e3      # 1500.0
tiny_float = 2.5e-4           # 0.00025
infinity = 1e999              # too big for a float -> inf
not_a_number = infinity - infinity   # nan
print(simple_float, type(simple_float))
print(scientific_float, tiny_float)
print(infinity, not_a_number)
print(0.1 + 0.2)              # float precision issue

# ---------- complex ----------
complex_number = 2 + 3j
another_complex = 1 - 4j
print(complex_number, type(complex_number))
print(another_complex)
print(complex_number.real, complex_number.imag)

# ---------- bool (it is a subtype of int) ----------
true_value = True
false_value = False
print(true_value, type(true_value))
print(false_value)
print(true_value + true_value)   # True is 1, so 1 + 1 = 2

# ---------- mixing number types ----------
print(1 + 2.5, type(1 + 2.5))               # int + float -> float
print(1 + (2 + 3j), type(1 + (2 + 3j)))     # int + complex -> complex
print(True + 5, type(True + 5))             # bool + int -> int


# ---------- int ----------
decimal_int = 42
negative_int = -7
big_int = 10 ** 30            # no size limit in Python
binary_int = 0b1010           # binary -> 10
octal_int = 0o17              # octal  -> 15
hex_int = 0xFF                # hex    -> 255
readable_int = 1_000_000      # underscores for readability
print(decimal_int, type(decimal_int))
print(negative_int, big_int)
print(binary_int, octal_int, hex_int)
print(readable_int)

# ---------- float ----------
simple_float = 3.14
scientific_float = 1.5e3      # 1500.0
tiny_float = 2.5e-4           # 0.00025
infinity = 1e999              # too big for a float -> inf
not_a_number = infinity - infinity   # nan
print(simple_float, type(simple_float))
print(scientific_float, tiny_float)
print(infinity, not_a_number)
print(0.1 + 0.2)              # float precision issue

# ---------- complex ----------
complex_number = 2 + 3j
another_complex = 1 - 4j
print(complex_number, type(complex_number))
print(another_complex)
print(complex_number.real, complex_number.imag)

# ---------- bool (it is a subtype of int) ----------
true_value = True
false_value = False
print(true_value, type(true_value))
print(false_value)
print(true_value + true_value)   # True is 1, so 1 + 1 = 2

# ---------- mixing number types ----------
print(1 + 2.5, type(1 + 2.5))               # int + float -> float
print(1 + (2 + 3j), type(1 + (2 + 3j)))     # int + complex -> complex
print(True + 5, type(True + 5))             # bool + int -> int








# =====================================================================
# LIBRARIES SECTION
# Extra number types that need an import (both come with Python,
# nothing to install with pip).
# =====================================================================
 
# ---------- Library: decimal -> type: Decimal ----------
# What it is for: exact decimal arithmetic (money, prices, precise math).
# How to use it:
#   1. Import it:  from decimal import Decimal
#   2. Create values from STRINGS (a float would already carry its error)
#   3. Operate with +, -, *, / like normal numbers
from decimal import Decimal
 
decimal_a = Decimal("0.1")
decimal_b = Decimal("0.2")
print(decimal_a + decimal_b, type(decimal_a))   # 0.3 (exact, unlike float)
print(Decimal("10.25") * 3)                     # 30.75
 
# ---------- Library: fractions -> type: Fraction ----------
# What it is for: exact rational numbers (numerator / denominator).
# How to use it:
#   1. Import it:  from fractions import Fraction
#   2. Create with Fraction(numerator, denominator) or Fraction("1/3")
#   3. Operate with +, -, *, / and the result stays an exact fraction
from fractions import Fraction
 
fraction_a = Fraction(1, 3)
fraction_b = Fraction(1, 6)
print(fraction_a + fraction_b, type(fraction_a))  # 1/2
print(Fraction("3/4") * 2)                        # 3/2
