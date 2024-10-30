import numpy as np
from scipy.integrate import odeint

# Constants
d0 = 30   # Positive constant for demand
d1 = 2    # Price sensitivity of demand
d2 = 4    # Sensitivity of demand to expected price changes
s0 = 20   # Positive constant for supply
s1 = 1    # Price sensitivity of supply
s2 = 6    # Sensitivity of supply to expected price changes
l = 0.1   # Speed of adjustments (a positive number)

# Equilibrium price
p_star = (d0 + s0) / (d1 + s1)

# Market clearing condition for the numerical example
def market_clearing(p, t):
    qd = d0 - d1 * p + d2 * 0  # Initial p' = 0 for simplicity
    qs = -s0 + s1 * p - s2 * 0  # Initial p' = 0 for simplicity
    return l * (qd - qs)

# Initial price
p0 = 5  # Initial price at t=0
t = np.linspace(0, 100, 500)  # Time array from 0 to 100 months

# Solve the differential equation
p_solution = odeint(market_clearing, p0, t)

# Print results
print(f'Equilibrium Price (p*): {p_star:.2f}')
for i in range(0, len(t), 100):  # Print price at intervals
    print(f'Price at t={t[i]:.2f} months: {p_solution[i][0]:.2f}')
