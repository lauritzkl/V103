import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

V1, y, x = np.genfromtxt('data4.1.txt', unpack=True)

def f(x, a, b):
    return a * x + b

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(-0.01, 0.2, 6)

plt.plot(x, y, 'kx', label='Daten')
plt.plot(x_plot, f(x_plot, *params), 'r-', label='Linearer Fit')
plt.legend()
plt.grid()
plt.ylabel('D(x) in m')
plt.xlabel('*')
plt.show()
#plt.savefig('ausgleichsgerade.pdf')
print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
