import numpy as np
from scipy.integrate import odeint

# Constants
d0 = 30   # positive constant
d1 = 2    # positive constant
d2 = 4    # positive constant for expectations
s0 = 20   # positive constant
s1 = 1    # positive constant
s2 = 6    # positive constant for expectations
l = -1    # speed of adjustments (l < 0)

# Equilibrium price
p_star = (d0 + s0) / (d1 + s1)

# New price adjustment equation with expectations
def price_adjustment_with_expectations(p, t):
    p_prime = 0  # In dynamic equilibrium, the derivative of price is zero
    qd = d0 - d1 * p + d2 * p_prime  # Demand function
    qs = -s0 + s1 * p - s2 * p_prime  # Supply function
    return l * (qd - qs)

# Initial price
p0 = 5  # Initial price at t=0
t = np.linspace(0, 10, 100)  # Time array from 0 to 10 months

# Solve the differential equation
p_solution = odeint(price_adjustment_with_expectations, p0, t)

# Print the equilibrium price
print(f'Equilibrium Price (p*): {p_star:.2f}')
