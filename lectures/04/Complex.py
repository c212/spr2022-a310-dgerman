class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        return str(self.real) + " + i * " + str(self.imag)
    def plus(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
