import math

class ComplexNumber(object):
    """
    This object defines a complex number, which can be used to calculate
    the standard operations in math for complex numbers.
    
    Attributes:
    real (float): the real element of the complex number
    im (float): the imaginary element of the complex number
    """
    def __init__(self, real, im):
        self.real = real
        self.im= im
        
    def conjugate(self):
        return ComplexNumber(self.real, -self.im)
    
    def __abs__(self):
        return math.sqrt(self.real**2 + self.im**2)
    
    def __lt__(self, other):
        if abs(self)<abs(other):
            return True
        else:
            return False
        
    def __gt__(self, other):
        if abs(self)>abs(other):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if (self.real==other.real) and (self.im==other.im):
            return True
        else:
            return False
        
    def __ne__(self, other):
        if not (self==other):
            return True
        else:
            return False
        
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.im + other.im)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.im - other.im) 
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real*other.real - self.im*other.im, self.real*other.im + self.im*other.real)
        else:
            return ComplexNumber(self.real*other, self.im*other)
        
    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            numerator = self * other.conjugate()
            denominator = other * other.conjugate()
            denominator = denominator.real
            return numerator/denominator
        else:
            return ComplexNumber(self.real/other, self.im/other)
        
    def __repr__(self):
        return  "%s + %si" % (self.real, self.im)