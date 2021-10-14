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


print(div.solve(input("n : "), input('d : '))) 