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
        d = rezs[3]; d0 = imzs[3]
        e = rezs[4]; e0 = imzs[4]
        
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
            real = (a*b*c*d)-(a*b*c0*d0)-(a*b0*c*d0)-(a*b0*c0*d)-(a0*b*c*d0)-(a0*b*c0*d)-(a0*b0*c*d)+(a0*b0*c0*d0)
            img = (a*b*c*d0)+(a*b*c0*d)+(a*b0*c*d)-(a*b0*c0*d0)+(a0*b*c*d)-(a0*b*c0*d0)-(a0*b0*c*d0)-(a0*b0*c0*d)
            result = f'{real}+{img}i'
            if (img<0):
                result = result.replace("+","")
            
        if (long == longb == 5):
            real = (a*b*c*d*e)-(a*b*c0*d0*e)-(a*b*c*d0*e0)-(a*b*c0*d*e0)-(a0*b0*c*d*e)+(a0*b0*c0*d0*e)+(a0*b0*c*d0*e0)+(a0*b0*c0*d*e0)-(a*b0*c*d*e0)+(a*b0*c0*d0*e0)-(a*b0*c*d0*e)-(a*b0*c0*d*e)-(a0*b*c*d*e0)+(a0*b*c0*d0*e0)-(a0*b*c*d0*e)-(a0*b*c0*d*e)
            img = (a*b*c*d*e0)-(a*b*c0*d0*e0)+(a*b*c*d0*e)+(a*b*c0*d*e)-(a0*b0*c*d*e0)+(a0*b0*c0*d0*e0)-(a0*b0*c*d0*e)-(a0*b0*c0*d*e)+(a*b0*c*d*e)-(a*b0*c0*d0*e)-(a*b0*c*d0*e0)-(a*b0*c0*d*e0)+(a0*b*c*d*e)-(a0*b*c0*d0*e)-(a0*b*c*d0*e0)-(a0*b*c0*d*e0)
            result = f'{real}+{img}i'
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
            
        a = rezs[0]; a0 = imzs[0] 
        b = rezs[1]; b0 = imzs[1]
        c = rezs[2]; c0 = imzs[2]
        
        long = len(rezs)
        longb = len(imzs)
        
        if (long == longb == 2):
            real = (a*b)+(a0*b0)
            img = (b*a0)-(a*b0)
            denom = (b**2)+(b0**2)
            result = f'{real}/{denom} + {img}/{denom}i'
            if (img<0):
                result = result.replace("+","")
            
        if (long == longb == 3):
            real = ((a*b*c)-(a*b0*c0)+(a0*b*c0)+(a0*b0*c))
            img = ((a0*b*c)-(a0*b0*c0)-(a*b*c0)-(a*b0*c))
            denom = (((b*c)-(b0*c0)**2)+((b*c0)+(b0*c)**2))
            result = f'{real}/{denom} + {img}/{denom}i'
            if (img<0):
                result = result.replace("+","")
            
        if(longb == longb == 4):
            real = 0
            img = 0

        return result

operation = int(input("operation ="))

if (operation == 2):
    
    
    print(Complexes.addition())

if (operation == 3):
    
    
    print(Complexes.substraction())

if (operation == 4):
    
    
    print(Complexes.multiplication())

if (operation == 5):
    
    
    print(Complexes.division())
