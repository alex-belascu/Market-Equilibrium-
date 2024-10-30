import numpy as np
from scipy.integrate import odeint

# Constants
d0 = 30   # positive constant
d1 = 2    # positive constant
s0 = 20   # positive constant
s1 = 1    # positive constant
l = -1    # speed of adjustments (l < 0)

# Equilibrium price
p_star = (d0 + s0) / (d1 + s1)

# Price adjustment equation
def price_adjustment(p, t):
    qd = d0 - d1 * p  # Demand function
    qs = -s0 + s1 * p  # Supply function
    return l * (qd - qs)

# Initial price
p0 = 5  # Initial price at t=0
t = np.linspace(0, 10, 100)  # Time array from 0 to 10 months

# Solve the differential equation
p_solution = odeint(price_adjustment, p0, t)

# Print the equilibrium price
print(f'Equilibrium Price (p*): {p_star:.2f}')
