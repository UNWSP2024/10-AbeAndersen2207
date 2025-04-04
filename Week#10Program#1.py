#UNWSP Programming PythonCos2005DEsp25
#Program_2_Complex Number Class
#04.4.25
#Abraham. N. Andersen

class ComplexNumber:
    def __init__(self, real, imag):

        self.real = real
        self.imag = imag

    def __add__(self, other_complex):

        new_real = self.real + other_complex.real
        new_imag = self.imag + other_complex.imag

        return ComplexNumber(new_real, new_imag)

    def __str__(self):

        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, -2)
sum_complex = complex1 + complex2


print(f"First complex number: {complex1}")
print(f"Second complex number: {complex2}")
print(f"The sum is: {sum_complex}")