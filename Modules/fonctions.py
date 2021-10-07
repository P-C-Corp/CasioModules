from math import *
#ax+b=c
class degre1():
    def solve(equation):   
      try:
        if not "=" in equation:
          raise MemoryError
        if not "x" in equation:
          raise SyntaxError
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
      except SyntaxError:
        return 'Syntaxe Error, x not found in equation'
      except MemoryError:
        return('Syntaxe Error, = not found, entry is not equation')

class degre2():
  def solve(a, b, c, complexMode=False): #défini la fonction avce les constantes et le mode complexe (désactivé par défaut)
    try:
      a= float(a) #
      b=float(b)  # converti les constantes en nombre au cas ou
      c=float(c)  #
      delta = (b**2) - (4*a*c) # calcul de delta
      if delta > 0: #cas supérieur à 0
        x1 = (-b-sqrt(delta))/(2*a) #calcul des racines
        x2 = (-b+sqrt(delta))/(2*a) # 
        return [x1, x2] #renvoie les racines à la ligne d'appel
      elif delta == 0: #cas égal 0
        x = (-b)/(2*a) #calcul de la racine
        return [x]
      elif delta < 0 and complexMode: #delta negatif et solution complexes demandées
        z1 = str((-b)/(2*a)) + '+i' + str(abs(sqrt(-delta)/2*a)) 
        z2 = str((-b)/(2*a)) + '-i' + str(abs(sqrt(-delta)/2*a))
        return [z1, z2]
      else:
        return None #delta négatif pas de solutio

    except TypeError or ValueError:
      return 'Error, invalid parameter' #gestion des erreurs relatives aux valeurs



print(degre2.solve(input('a'), input('b'), input('c')))
