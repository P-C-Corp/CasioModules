from math import*

#rules
print('Enter 0 when you want to answer no to the question')
print('Enter 1 when you want to answer yes to the question')
print('Enter 2 for addition')
print('Enter 3 for substraction')
print('Enter 4 for multiplication')
print('Enter 5 for division')

class Complexes():
    def liste():
        Complexe = []
        i = complex (0,1)
        Complex = True
        if (Complex==True):
            
            Rez = float(input('Rez='))
            Imz = float(input('Imz='))
            Complex1 = f"{Rez}+i{Imz}"
            Complexe.append(Complex1)
            c = int(input('Wanna other complexe? ='))
            
            if (c==True):
                
                b = int(input('Number of other complexe you want ='))
                while (b > 0):
                    #DefinitLeComplexe = int(input('Enter 1 ='))
                    Rez = float(input('Rez='))
                    Imz = float(input('Imz='))
                    Complex1 = f"{Rez}+i{Imz}"
                    Complexe.append(Complex1)
                    b -= 1

                    if (b==0):
                        break
                
        return (Complexe)

    def addition():
        numbers = Complexes.liste() 
        rezs = {}
        imzs = {}
        rank = 0
        for i in numbers:
            a = i.split("+")
            
            rezs[rank] = float(a[0]) #explique pk a[0] d'où vient le 0 et le a ?
            imzs[rank] = float(a[1].replace ("i","")) #explique pk a[1] d'où vient le 1 et le a ?
            rank += 1
        real = 0
        img = 0
        for rez in rezs.keys():
            real = real + float(rezs[rez])
        for imz in imzs.keys():
            img = img + float(imzs[imz])
            
        result = f"{real}+{img}i"
        if (img<0):
            result = result.replace('+', '')
        return result

    def substraction ():
        numbers = Complexes.liste()
        rezs = {}
        imzs = {}
        rank = 0
        for i in numbers:
            a = i.split("+")
            
            rezs[rank] = float(a[0]) # explique pk a et 0 d'où ça vient ?
            imzs[rank] = float(a[1].replace("i","")) #pareil pour le 1

            rank += 1
            
            
        
        real = 0
        img = 0
        for rez in rezs.keys():
            real = -real - float(rezs[rez])
        for imz in imzs.keys():
            img = -img - float(imzs[imz])
            
        result = f"{real}+{img}i"
        if (img<0):
            result = result.replace("+","")
        return result

operation = int(input("operation ="))

if (operation == 2):
    
    
    print(Complexes.addition())

if (operation == 3):
    
    
    print(Complexes.substraction())

"""# GROS PROBLEME:
le programme n'arrive pas à additiuonner et soustraire deux complexes identiques.
Au lieu de les additionner et soustraires il renvoit juste l'un des deux :/"""
