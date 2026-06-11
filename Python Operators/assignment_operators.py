# ------------------------------------------------------------
# 1. = (Simple Assignment)
# ------------------------------------------------------------
# Assigns the value on the right to the variable on the left.
# This is the most basic operator in Python.

x = 5
print("= (Simple Assignment)")
print(f"  x = 5  →  x is now: {x}")         # Output: 5
print()


# ------------------------------------------------------------
# 2. += (Addition Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x + 3
# Takes the current value of x, adds 3, and stores the result
# back into x.

x = 5
x += 3
print("+= (Addition Assignment)")
print(f"  x = 5, then x += 3  →  x is now: {x}")   # Output: 8
print()


# ------------------------------------------------------------
# 3. -= (Subtraction Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x - 3
# Takes the current value of x, subtracts 3, and stores the
# result back into x.

x = 5
x -= 3
print("-= (Subtraction Assignment)")
print(f"  x = 5, then x -= 3  →  x is now: {x}")   # Output: 2
print()


# ------------------------------------------------------------
# 4. *= (Multiplication Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x * 3
# Multiplies the current value of x by 3 and stores the result
# back into x.

x = 5
x *= 3
print("*= (Multiplication Assignment)")
print(f"  x = 5, then x *= 3  →  x is now: {x}")   # Output: 15
print()


# ------------------------------------------------------------
# 5. /= (Division Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x / 3
# Divides the current value of x by 3 and stores the result
# back into x. Always returns a FLOAT (decimal number).

x = 5
x /= 3
print("/= (Division Assignment)")
print(f"  x = 5, then x /= 3  →  x is now: {x}")   # Output: 1.6666...
print()


# ------------------------------------------------------------
# 6. %= (Modulus Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x % 3
# Divides x by 3 and stores only the REMAINDER back into x.
# Great for checking even/odd numbers or cycling values.

x = 5
x %= 3
print("%= (Modulus Assignment)")
print(f"  x = 5, then x %= 3  →  x is now: {x}")   # Output: 2  (5 ÷ 3 = 1 remainder 2)
print()


# ------------------------------------------------------------
# 7. //= (Floor Division Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x // 3
# Divides x by 3 and stores the result rounded DOWN to the
# nearest whole number (integer). Also called integer division.

x = 5
x //= 3
print("//= (Floor Division Assignment)")
print(f"  x = 5, then x //= 3  →  x is now: {x}")  # Output: 1  (5 ÷ 3 = 1.666 → rounded down to 1)
print()


# ------------------------------------------------------------
# 8. **= (Exponentiation Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x ** 3
# Raises x to the power of 3 (x³) and stores the result
# back into x.

x = 5
x **= 3
print("**= (Exponentiation Assignment)")
print(f"  x = 5, then x **= 3  →  x is now: {x}")  # Output: 125  (5³ = 5 × 5 × 5)
print()


# ============================================================
#   BITWISE ASSIGNMENT OPERATORS
# ============================================================
# The following operators work on the BINARY representation
# of integers (bits: 0s and 1s).
#
# Quick reference:
#   5  in binary  →  0101
#   3  in binary  →  0011
# ============================================================


# ------------------------------------------------------------
# 9. &= (Bitwise AND Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x & 3
# Compares each bit of x and 3. The result bit is 1 only if
# BOTH corresponding bits are 1, otherwise 0.
#
#   5  →  0101
#   3  →  0011
#   &  →  0001  =  1

x = 5
x &= 3
print("&= (Bitwise AND Assignment)")
print(f"  x = 5 (0101), then x &= 3 (0011)  →  x is now: {x}")  # Output: 1
print()


# ------------------------------------------------------------
# 10. |= (Bitwise OR Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x | 3
# Compares each bit of x and 3. The result bit is 1 if
# EITHER (or both) corresponding bits are 1.
#
#   5  →  0101
#   3  →  0011
#   |  →  0111  =  7

x = 5
x |= 3
print("|= (Bitwise OR Assignment)")
print(f"  x = 5 (0101), then x |= 3 (0011)  →  x is now: {x}")  # Output: 7
print()


# ------------------------------------------------------------
# 11. ^= (Bitwise XOR Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x ^ 3
# XOR = "exclusive OR". The result bit is 1 only if the
# two corresponding bits are DIFFERENT (one 0, one 1).
#
#   5  →  0101
#   3  →  0011
#   ^  →  0110  =  6

x = 5
x ^= 3
print("^= (Bitwise XOR Assignment)")
print(f"  x = 5 (0101), then x ^= 3 (0011)  →  x is now: {x}")  # Output: 6
print()


# ------------------------------------------------------------
# 12. >>= (Bitwise Right Shift Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x >> 3
# Shifts all bits of x to the RIGHT by 3 positions.
# Bits that fall off the right are discarded.
# Each right shift by 1 is roughly equivalent to dividing by 2.
#
#   5  →  0000 0101
#   >> 3 → 0000 0000  =  0  (all bits shifted past position 0)

x = 5
x >>= 3
print(">>= (Bitwise Right Shift Assignment)")
print(f"  x = 5 (0b0101), then x >>= 3  →  x is now: {x}")  # Output: 0
print()


# ------------------------------------------------------------
# 13. <<= (Bitwise Left Shift Assignment)
# ------------------------------------------------------------
# Equivalent to: x = x << 3
# Shifts all bits of x to the LEFT by 3 positions.
# New bits on the right are filled with 0s.
# Each left shift by 1 is roughly equivalent to multiplying by 2.
#
#   5  →  0000 0101
#   << 3 → 0010 1000  =  40  (5 × 2³ = 5 × 8 = 40)

x = 5
x <<= 3
print("<<= (Bitwise Left Shift Assignment)")
print(f"  x = 5 (0b0101), then x <<= 3  →  x is now: {x}")  # Output: 40
print()


# ------------------------------------------------------------
# 14. := (Walrus Operator / Assignment Expression)
# ------------------------------------------------------------
# Introduced in Python 3.8.
# Unlike all other assignment operators, := ASSIGNS a value
# to a variable AND RETURNS that value at the same time —
# all within a single expression.
#
# This is especially useful inside conditions and loops,
# so you don't need a separate assignment line.
#
# Example 1: Basic usage inside print()
print(":= (Walrus Operator / Assignment Expression)")
print(f"  print(x := 3)  →  x is now: ", end="")
print(x := 3)                                        # Output: 3

# Example 2: Useful real-world pattern — assign and check in one step
numbers = [1, 8, 3, 15, 4, 9]
print(f"\n  Real-world example — find first number > 7 in {numbers}:")
for n in numbers:
    if (found := n) > 7:           # assigns n to 'found' AND checks if > 7
        print(f"  First number greater than 7 is: {found}")
        break
print()


# ============================================================
#                     SUMMARY TABLE
# ============================================================
print("=" * 55)
print(f"  {'Operator':<10} {'Example':<15} {'Equivalent To':<20}")
print("=" * 55)

operators = [
    ("=",   "x = 5",    "x = 5"),
    ("+=",  "x += 3",   "x = x + 3"),
    ("-=",  "x -= 3",   "x = x - 3"),
    ("*=",  "x *= 3",   "x = x * 3"),
    ("/=",  "x /= 3",   "x = x / 3"),
    ("%=",  "x %= 3",   "x = x % 3"),
    ("//=", "x //= 3",  "x = x // 3"),
    ("**=", "x **= 3",  "x = x ** 3"),
    ("&=",  "x &= 3",   "x = x & 3"),
    ("|=",  "x |= 3",   "x = x | 3"),
    ("^=",  "x ^= 3",   "x = x ^ 3"),
    (">>=", "x >>= 3",  "x = x >> 3"),
    ("<<=", "x <<= 3",  "x = x << 3"),
    (":=",  "x := 3",   "assigns + returns"),
]

for op, example, equiv in operators:
    print(f"  {op:<10} {example:<15} {equiv:<20}")

print("=" * 55)
