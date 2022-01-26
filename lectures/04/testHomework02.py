from Fraction import Fraction
from Complex import Complex

f1 = Fraction(3, 5)
c1 = Complex(3, 5)

f2 = Fraction(-2, 5)
print(f1 + f2) # 5/25

c2 = Complex(-3, -5)
print(c2 + c1) # 0 + i * 0
