from Fraction import Fraction
from Complex import Complex

f1 = Fraction(3, 5)
c1 = Complex(3, 5)

f2 = Fraction(-2, 5)
print(str(f1.plus(f2))) # 5/25

c2 = Complex(-3, -5)
print(str(c2.plus(c1))) # 0 + i * 0
