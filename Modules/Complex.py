from math import*

#rules
print('Enter 1 when you want to answer yes to the question')
print('Enter 0 when you want to answer no to the question')

class Complexes():
    def Liste():
        #pour utiliser ou quitter le programme
        Origine = float(input('Wanna use the program? ='))
        
        if (Origine==True):
            #definir la liste de complexes
            Complexe = []
            #valeur de i = sqrt(-1)
            i = complex (0,1)
            #pour définir le premier complexe
            Complex = int(input("Wanna definit a complexe? ="))
            #conditions
            if (Complex==False):
                #marque l'erreur
                ##Chercher comment reboucler le programme
                raise SyntaxError('must enter 1 for yes to definit it')
            elif (Complex==True):
                #premier complexe
                DefinitLeComplexe = int(input('Just enter 1='))
                #au cas où un idiot ne sait pas suivre des instructions
                if (DefinitLeComplexe != 1):
                    raise SyntaxError('Told you faggot')
                #définition de la partie réele t imaginaire du complexe
                Rez = float(input('Rez='))
                Imz = float(input('Imz='))
                Complex1 = f"{Rez}+j{Imz}"
                #ajout du complexe à la liste
                Complexe.append(Complex1)
                #si ne veux pas d'autre complexe
                c = int(input('Wanna other complexe? ='))
                if (c==True):
                    #valeur pour arrêter le programme
                    b = int(input('Number of other complexe you want ='))
                    #boucle pour les autres complexes
                    while (DefinitLeComplexe==True):
                        DefinitLeComplexe = int(input('Enter 1 ='))
                        #si l'idiot ne sais toujours pas suivre une consigne
                        if (DefinitLeComplexe != 1):
                            raise SyntaxError('Told you faggot')
                        # définition des parties réels et imaginaires des autres complexes
                        Rez = float(input('Rez='))
                        Imz = float(input('Imz='))
                        Complex1 = f"{Rez}+j{Imz}"
                        #ajout à la liste de ses derniers
                        Complexe.append(Complex1)
                        #pour stopper la boucle au nombre de complexe voulu
                        b -= 1
                        #littéralement casser la boucle
                        if (b==0):
                            break
                    else:
                        pass
            #affiche la liste
            return (Complexe)
        
        elif (Origine==False):
            raise SyntaxError('must enter 1 for yes to use it')


Liste = (Complexes.Liste())
print(Liste)
lenListe = len(Liste)
rezs = {}
imgs = {}
for i in Liste:
    print (f"{Liste.index(i)} -> {i} ")
    a = i.split("+")
    rezs[i] = a[0]
    imgs[i] = a[1].replace ("j","")
#print (rezs)
#print (imgs)
wanted = Liste.pop(int(input('Nombre 1 = ?')))
print (wanted)
print(rezs[wanted])