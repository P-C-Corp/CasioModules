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
#pour le nb de complexe à sortir

wantede = Liste.pop(int(input('Nombre 1 = ?')))
print (wantede)
print(rezs[wantede])
print(imzs[wantede])