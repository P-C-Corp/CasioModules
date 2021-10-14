from math import*
from random import*

class SA():
    def solve(formula,n):
        if not 'n'in formula:
            raise SyntaxError('no n found in formula')
        try:
            float(n)
        except ValueError or TypeError:
            raise ValueError('n must be number')
        return n


print(SA.solve(input('formula : '), input('n : ')))