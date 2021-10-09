from math import *
#équations de degré 1
class degre1():
    def solve(equation):   
      if not "=" in equation:                                                           #
        raise SyntaxError("No '=' found in formula, equation degre 1 must be ax+b=c")   # verifie si l'entrée est une équation
      if not "x" in equation:                                                           #
        raise SyntaxError("No 'x' found in equation, equation degre 1 must be ax+b=c ") #
      line = equation.replace(' ', "")  #
      line = line.replace('(', "")      #
      line = line.replace(')', "")      # formatage de l'équation sous forme ax+b=c sans espace/doubles opérateurs/parenthèses
      line = line.replace('+-', "-")    #
      line = line = line.split("=")   # sépare l'équation au niveau du = pour isoler c
      c = float(line[1])      # stocke c sous forme de nombre   
      ab = line[0]            # stacke ax+b sous forme de string 
      if "-" in ab:     #si l'opération est une soustraction
        operator = ab.find('-') #sépare ax et b au niveau du moins
        a = ab[:operator].replace('x',"")   # récupère tous les caractères jusqu'à l'opérateur et enlève x pour isoler a 
        if a != '': # vérifie que a ≠ 0
          a = float(a) # si oui, le converti en nombre
        else:
          raise ValueError("Entry is not equation, a can't be 0") # sinon, renvoie une erreur
        ab = ab.split('-') #sépare ax+b pour isoler b
        b = -1*(float(ab[1])) #stocke b sous forme de nombre | * -1 car l'opérateur est '-'
      elif "+" in ab: # meme chose si l'opérateur est positif (sauf que pas besoin de changer le signe de ||b||)
        operator = ab.find('+')
        a = float(ab[:operator - 1].replace('x',""))
        a = ab[:operator].replace('x',"")
        if a != '':
          a = float(a)
        else:
          return ('a = 0, No solutions')
        ab = ab.split('+')
        b = (float(ab[1]))
      else: # pas d'opérateur (b = 0)
        a = float(ab.replace('x','')) # isole a sans x
      b = 0
      x = (c-b)/a
      try:
        int(x) # enlève le .0  si x est entier de façon plus conventionelle (;
      except ValueError:
        pass
      return x

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
        return [delta, x1, x2] #renvoie les racines à la ligne d'appel
      elif delta == 0: #cas égal 0
        x = (-b)/(2*a) #calcul de la racine
        return [delta, x]
      elif delta < 0 and complexMode: #delta negatif et solution complexes demandées
        z1 = str((-b)/(2*a)) + '+i' + str(abs(sqrt(-delta)/2*a)) 
        z2 = str((-b)/(2*a)) + '-i' + str(abs(sqrt(-delta)/2*a))
        return [delta, z1, z2]
      else:
        return [delta] #delta négatif pas de solution(s)

    except TypeError or ValueError:
      raise ValueError('An error occured, please check your entries') #gestion des erreurs relatives aux valeurs

  def canon(a, b, c):
    roots = degre2.solve(a, b, c, False)
    a= float(a) #
    b=float(b)  # converti les constantes en nombre au cas ou
    c=float(c)  #
    beta = b/(2*a)
    delta = roots[0]
    if delta < 0:
      raise ValueError('Delta is negative')
    alpha = delta/(4*(a**2))
    canonic = f"{a}[(x+{beta})-{alpha}]"
    if a == 1:
      canonic = canonic.replace(f"{a}[", "")
      canonic = canonic.replace(f"]", "")
    if alpha == 0:
      canonic = canonic.replace(f"-{alpha}", "")
    canonic = canonic.replace('+-', "-")
    canonic = canonic.replace('--', "+")
    return canonic



print(degre2.canon(input('a'), input('b'), input('c')))

