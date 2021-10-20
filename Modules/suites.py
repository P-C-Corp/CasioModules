from math import*

class suites():
    def solve(formula,n):
        operators = "*+-/()"
        if not 'n'in formula:
            raise SyntaxError('no n found in formula')
        try:
            n = int(n)
        except ValueError or TypeError:
            raise ValueError('n must be integer')
        
        for i in formula:
            if i == "n":
                pos = formula.index(i)
                if not formula[pos - 1] in operators and pos !=0:
                    raise SyntaxError('Operators must be explicitly specified, even *')
                else: 
                    result = eval(formula.replace('n', str(n)))
        return result

    def somme(formula,number, p=0):
        operators = "*+-/()"
        if not 'n'in formula:
            raise SyntaxError('no n found in formula')
        try:
            number = int(number)
            p = int(p)
        except ValueError or TypeError:
            raise ValueError('n (and first term if there is one) must be integer(s)')
        for i in formula:
            if i == "n":
                pos = formula.index(i)
                if not formula[pos - 1] in operators and pos != 0:
                    raise SyntaxError('Operators must be explicitly specified, even *')
                else:
                    pass
        somme = 0
        for number in range(p, number+1):
            nouveauTerme = suites.solve(formula, number)
            somme = somme+nouveauTerme
        return somme
print(suites.somme(input('formula : '), input('n : ')))