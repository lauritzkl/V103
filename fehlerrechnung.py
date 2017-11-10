import numpy as np
from uncertainties import ufloat

m_1 = ufloat(33.557e-3, 0.547e-3)
m_2 = ufloat(59.623e-3, 3.313e-3)
m_3 = ufloat(5.761e-3, 0.305e-3)
m_31 = ufloat(4.893e-3, 0.207e-3)
m_4 = ufloat(11.580e-3, 0.299e-3)
m_41 = ufloat(11.599e-3, 0.337e-3)
I_1 = ufloat(8.81e-10, 0.10e-10)
I_2 = ufloat(490.87e-12, 0)

print('E_1=', 5.243/(2*m_1*I_1))
print('E_2=', 5.243/(2*m_2*I_2))
print('E_3=', 23.171/(48*m_3*I_1))
print('E_31=', 23.171/(48*m_31*I_1))
print('E_4=', 23.171/(48*m_4*I_2))
print('E_41=', 23.171/(48*m_41*I_2))
