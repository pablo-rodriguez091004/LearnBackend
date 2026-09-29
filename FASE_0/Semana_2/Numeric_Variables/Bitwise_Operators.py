# BITWISE OPERATORS
# Work on the binary representation of integers, bit by bit.

a = 0b1100    # 12
b = 0b1010    # 10

print("a      =", a, "->", bin(a))
print("b      =", b, "->", bin(b))

# AND (&) -> 1 only where both bits are 1
print("a & b  =", a & b, "->", bin(a & b))      # 8  (0b1000)

# OR (|) -> 1 where at least one bit is 1
print("a | b  =", a | b, "->", bin(a | b))      # 14 (0b1110)

# XOR (^) -> 1 where the bits are different
print("a ^ b  =", a ^ b, "->", bin(a ^ b))      # 6  (0b110)

# NOT (~) -> flips every bit (result is -(a + 1))
print("~a     =", ~a)                           # -13

# Left shift (<<) -> moves bits left (same as multiplying by 2 each step)
print("a << 1 =", a << 1)                       # 24
print("a << 2 =", a << 2)                       # 48

# Right shift (>>) -> moves bits right (same as dividing by 2 each step)
print("a >> 1 =", a >> 1)                       # 6
print("a >> 2 =", a >> 2)                       # 3

# Common uses
number = 13
print("13 is odd  :", (number & 1) == 1)        # True (last bit is 1)
print("13 * 8     :", number << 3)              # 104
print("13 // 4    :", number >> 2)              # 3

# Flags with bit masks
READ = 0b100
WRITE = 0b010
EXECUTE = 0b001
permissions = READ | WRITE
print("permissions      :", bin(permissions))               # 0b110
print("can write?       :", (permissions & WRITE) != 0)     # True
print("can execute?     :", (permissions & EXECUTE) != 0)   # False