class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def plus(self, other):
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)
    
