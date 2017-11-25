import matplotlib as mpl
mpl.use('pgf')
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

V1, y, x = np.genfromtxt('data4.1.txt', unpack=True)

def f(x, a, b):
    return a * x + b

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(-0.01, 0.2, 6)

plt.plot(x, y, 'kx', label='Messwerte')
plt.plot(x_plot, f(x_plot, *params), 'r-', label='Regression')
plt.legend()
plt.grid()
plt.ylabel(r'$D(x) \, \text{in} \, \si{\meter}$')
plt.xlabel(r'$\left( 4x^3-12Lx^2+9L^2x-L^3 \right) \, \text{in} \, \si{\meter\tothe{3}}$')
plt.tight_layout()
plt.savefig('ausgleichsgerade4.1.pdf')
print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
