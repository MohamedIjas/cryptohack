# Importing the crt function from sympy.ntheory module
from sympy.ntheory.modular import crt

# Lists of moduli and remainders
moduli = [5, 11, 17]    # The moduli
remainders = [2, 3, 5]  # The corresponding remainders

# Using the crt function to find the solution to the system of congruences
result = crt(moduli, remainders)

# Print the result
print(result)
