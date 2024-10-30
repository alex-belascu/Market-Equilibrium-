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

# Market clearing condition
def market_clearing(p, t):
    p_prime = 0  # Assuming we're looking for a stable price
    qd = d0 - d1 * p + d2 * p_prime  # Demand function
    qs = -s0 + s1 * p - s2 * p_prime  # Supply function
    return l * (qd - qs)  # Return the rate of change of price

# Initial price
p0 = 5  # Initial price at t=0
t = np.linspace(0, 10, 100)  # Time array from 0 to 10 months

# Solve the differential equation
p_solution = odeint(market_clearing, p0, t)

# Print the equilibrium price and the price at the final time
print(f'Equilibrium Price (p*): {p_star:.2f}')
print(f'Price at t=10 months: {p_solution[-1][0]:.2f}')
