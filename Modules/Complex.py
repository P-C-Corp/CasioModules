from math import*

#rules
print('Enter 1 when you want to answer yes to the question')
print('Enter 0 when you want to answer no to the question')

class Complexes():
    def Liste():
        Complexe = []
        i = complex (0,1)
        Complex = int(input("Wanna definit a complexe? ="))
        if (Complex==True):
            DefinitLeComplexe = int(input('Just enter 1='))
            Rez = float(input('Rez='))
            Imz = float(input('Imz='))
            Complex1 = f"{Rez} + i {Imz}"
            Complexe.append(Complex1)
            c = int(input('Wanna other complexe? ='))
            if (c==True):
                b = int(input('Number of other complexe you want ='))
                while (DefinitLeComplexe==True):
                    DefinitLeComplexe = int(input('Enter 1 ='))
                    Rez = float(input('Rez='))
                    Imz = float(input('Imz='))
                    Complex1 = f"{Rez} + i {Imz}"
                    Complexe.append(Complex1)
                    b -= 1
                    if (b==0):
                        break
        return (Complexe)

Liste = (Complexes.Liste())
print(Liste)
lenListe = len(Liste)
rezs = {}
imzs = {}
for i in Liste:
    print (f"{Liste.index(i)} -> {i} ")
    a = i.split("+")
    rezs[i] = a[0]
    imzs[i] = a[1].replace ("j","")


wanted = []
d = int(input("Number of complexe needed ="))
e = 0
while (e==0): # met while True: ça suffi et c'est plus clean
    wanted.append(Liste.pop(int(input('Nombre (1er de la liste est 0)= '))))
    d -= 1
    if (d==0):
        break

print (wanted)
#print(rezs[wanted]) # aucun sens tu demande la partie réelle/imaginaire d'une liste de valeurs...
#print(imzs[wanted]) 

#un crée d'autres dicos et met tes valueurs en analysant ta liste au cas par cas :

wanted_rezs = {} #
wanted_imzs = {} # crée deux variables pour stocker les parties des nombres
for i in wanted:
    a = i.split("+") # sépare les parties
    wanted_rezs[i] = a[0] # stocke la partie réelle
    wanted_imzs[i] = a[1].replace ("j","") # stocke la partie imaginaire après avoir enlevé le "j" -> permet les opérations

"""
Principe du dico en python :
mon_dico = {}
le format est {clé1: val1, clé2: val2, etc.}

les valeurs s'appellent avce leur clé comme pour une liste avec l'index
exemple :
print(mon_dico[clé1])
>>>val1

pour récupérer une partie d'un nombre :

le format est {'complexe en forme str': la partie réelle oiu complexe selon le dico}

exemple:
Liste(Complexes.Liste())
-> script pour séparer
-> imprime les nombres et leur index
-> crée le wanted et stocke les parties => du coup le premier tri sert à rien ?
print(wanted_rezs['5+j6'])

>>>5

"""
