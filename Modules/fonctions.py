import math
#ax+b=c
class degre1():
    def solve(equation):
        
        line = equation.replace(' ', "")
        line = line.replace('(', "")
        line = line.replace(')', "")
        line = line.replace('+-', "-")
        line = line = line.split("=")
        c = float(line[1])
        ab = line[0]
        if "-" in ab:
            operator = ab.find('-')
            a = ab[:operator].replace('x',"")
            if a != '':
                a = float(a)
            else:
                return ('a = 0, No solutions')
            bLenght = (len(ab) - 1 -operator)
            print(bLenght)
            b = float(ab[:bLenght].replace('x',""))
        elif "+" in ab:
            operator = ab.find('-')
            a = float(ab[:operator - 1].replace('x',""))
            b = float(ab[:-operator].replace('x',""))
        else:
            a = float(ab.replace('x',""))
        x = (c-b)/a
        print('a =', a)
        print('b = ', b)
        print('c = ', c)
        return(x, "solves the equation")
        #except ValueError or TypeError or IndexError:
        #    print('Error - Equation must be ax+b=c, please check your entry')

print(degre1.solve(input('Type your equation :')))