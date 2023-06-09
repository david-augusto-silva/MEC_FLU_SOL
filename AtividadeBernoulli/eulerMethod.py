import numpy as np
import matplotlib.pyplot as plt

# dados do problema

g = 32.2  # aceleração da gravidade (ft/s²)
d0 = 2.5 * (1 / 12)  # diâmetro do furo na base do tanque (ft)
A0 = (np.pi * d0 ** 2) / 4  # area do furo na base do tanque (ft)

# Define parameters
f = lambda t, s: np.exp(-t)  # ODE
h = 0.1  # Step size
t = np.arange(0, 1 + h, h)  # Numerical grid
s0 = -1  # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h * f(t[i], s[i])

plt.figure(figsize=(12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()
