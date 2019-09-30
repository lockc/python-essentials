# +, -, *, /, //, %, **
# The order of their appearance is not accidental.

## A ** (double asterisk) sign is an exponentiation (power) operator. Its left argument is the base, its right, the exponent.

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# The result produced by the division operator is always a float
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# A // (double slash) sign is an integer divisional operator. It differs from the standard / operator in two details:
# its result lacks the fractional part - it's absent (for integers), or is always equal to zero (for floats); this means that the results are always rounded;
# it conforms to the integer vs. float rule.

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)


# This is very important: rounding always goes to the lesser integer.
print(6 // 4)
print(6. // 4)

# Integer division can also be called floor division.
