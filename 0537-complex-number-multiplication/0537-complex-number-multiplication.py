class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a_real, a_imaginary = num1.split('+')
        b_real, b_imaginary = num2.split('+')
        a_imaginary, b_imaginary = a_imaginary[:-1], b_imaginary[:-1]
        
        res_real = int(a_real) * int(b_real) - int(a_imaginary) * int(b_imaginary)
        res_imaginary = int(a_real) * int(b_imaginary) + int(a_imaginary) * int(b_real)
        
        return str(res_real)+ '+' + str(res_imaginary) + 'i'