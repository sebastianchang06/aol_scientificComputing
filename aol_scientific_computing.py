import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from scipy.optimize import fsolve

months = np.array([1, 2, 3, 4, 5])
production = np.array([15000, 18000, 22000, 26000, 30000])

p = Polynomial.fit(months, production, 2)

a, b, c = p.convert().coef
print(f"Model: P(t) = {a}t^2 + {b}t + {c}")

def production_function(t):
    return a * t**2 + b * t + c - 25000

month_needed = fsolve(production_function, 0)[0]
print(f"EIGER needs to start building the new warehouse in month: {int(month_needed)}")

