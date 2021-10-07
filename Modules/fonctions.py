import math
#ax+b=c
class degre1():
    def solve(equation):   
      try:
        if not "=" in equation:
          raise ValueError
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
            ab = ab.split('-')
            b = -1*(float(ab[1]))
        elif "+" in ab:
            operator = ab.find('+')
            a = float(ab[:operator - 1].replace('x',""))
            a = ab[:operator].replace('x',"")
            if a != '':
                a = float(a)
            else:
                return ('a = 0, No solutions')
            ab = ab.split('+')
            b = (float(ab[1]))
        else:
          a = float(ab.replace('x',''))
          b = 0
        x = (c-b)/a
        x=str(x)
        if x.endswith(".0"):
          x = float(x)
          x = round(x)
        return x
      except ValueError or TypeError or IndexError:
        return('Error - Equation must be ax+b=c, please check your entry')
print(degre1.solve(input('Type your equation :')))
