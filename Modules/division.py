class div():
    def solve(n, d):
        try:
            n = int(n)
            d = int(d)
        except ValueError or TypeError:
            raise ValueError('Arguments must  be integer')
        r = n%d
        q = (n-r)/d
        try:
            r = int(r)
        except ValueError or TypeError:
            pass
        try:
            q = int(q)
        except ValueError or TypeError:
            pass
        return [q, r]

    def isDiv(n, d):
        try:
            n = int(n)
            d = int(d)
        except ValueError or TypeError:
            raise ValueError('Arguments must  be integer')
        if n%d == 0:
            return True
        else:
            return False

    def pgcd(a,b):
        """
        a et b sont 2 entiers
        renvoie le Plus Grand Diviseur Commun des 2 nombres
        """
        if a<0 or b<0:
            return div.pgcd(abs(a),abs(b))
        if b==0:
            if a==0:
                print ("Le PGCD de deux nombres nuls n'existe pas")
            else:
                return a
        else:
            return div.pgcd(b,a%b)
        
print(div.solve(input("n : "), input('d : '))) 