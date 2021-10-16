from math import*
from lycee import*

class SA():
    def solve(formula,n):
        if not 'n'in formula:
            raise SyntaxError('no n found in formula')
        try:
            float(n)
        except ValueError or TypeError:
            raise ValueError('n must be number')
        
        for i in formula:
            if i == "n":
                pos = formula.index(i)


print(SA.solve(input('formula : '), input('n : ')))