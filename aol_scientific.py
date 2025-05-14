import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from scipy.optimize import fsolve

# Sample data
months = np.array([1, 2, 3, 4, 5])  # Time (months)
production = np.array([15000, 18000, 22000, 26000, 30000])  # Production data

# Fit a polynomial of degree 2
p = Polynomial.fit(months, production, 2)

# Coefficients
a, b, c = p.convert().coef
print(f"Model: P(t) = {a}t^2 + {b}t + {c}")

# Define the production function for warehouse capacity
def production_function(t):
    return a * t**2 + b * t + c - 25000

# Find the month when production reaches 25000
month_needed = fsolve(production_function, 0)[0]
print(f"EIGER needs to start building the new warehouse in month: {int(month_needed)}")

