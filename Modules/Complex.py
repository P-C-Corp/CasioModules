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
            rezs[rank] = float(a[0])
            imzs[rank] = float(a[1].replace ("i",""))
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
            rezs[rank] = float(a[0])
            imzs[rank] = float(a[1].replace("i",""))
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

    def multiplication ():
        numbers = Complexes.liste()
        rezs = {}
        imzs = {}
        rank = 0
        for i in numbers:
            a = i.split("+")
            rezs[rank] = float(a[0])
            imzs[rank] = float(a[1].replace("i",""))
            rank += 1
            
        a = rezs[0]; a0 = imzs[0] 
        b = rezs[1]; b0 = imzs[1]
        c = rezs[2]; c0 = imzs[2]
        
        long = len(rezs)
        longb = len(imzs)
        
        if (long == longb == 2):
            real = (a*b)-(a0*b0)
            img = (a*b0)+(b*a0)
            result = f"{real}+{img}i"
            if (img<0):
                result = result.replace("+","")
            
            
        if (long == longb == 3):
            real = (a*b*c)-(a0*b0*c)-(a*b0*c0)-(a0*b*c0)
            img = (a*b0*c)+(a0*b*c)+(a*b*c0)-(a0*b0*c0)
            result = f'{real}+{img}i'
            if (img<0):
                result = result.replace("+","")
            
            
        if (long == longb == 4):
            v = 5
            reel1 = rezs.values()
            reel = list(reel1)
            imaginaire1 = imzs.values()
            imaginaire = list(imaginaire1)
            
            while (v>=3):
                print(a)
                print(a0)
                print(b)
                print(b0)
                real = (a*b)-(a0*b0)
                reel.append(real)
                img = (a*b0)+(b*a0)
                imaginaire.append(img)
                print(reel)
                print(imaginaire)
                if (3<=v>=4):
                    k=1
                    a = reel[0+2*k]; a0 = imaginaire[0+2*k] 
                    b = reel[1+2*k]; b0 = imaginaire[1+2*k] 
                    k+=1
                v -= 1
        result = f"{real}+{img}i"
        if (img<0):
                result = result.replace("+","")
                
        return result

    def division ():
        numbers = Complexes.liste()
        rezs = {}
        imzs = {}
        rank = 0
        for i in numbers:
            a = i.split("+")
            rezs[rank] = float(a[0])
            imzs[rank] = float(a[1].replace("i",""))
            rank += 1

operation = int(input("operation ="))

if (operation == 2):
    
    
    print(Complexes.addition())

if (operation == 3):
    
    
    print(Complexes.substraction())

if (operation == 4):
    
    
    print(Complexes.multiplication())

if (operation == 5):
    
    
    print(Complexes.division())
