from division import div
import math

quotient = div.solve()
class operations():
    def __init__(self) -> None:
        pi = math.pi
    def p(a,n):
        return a**n

    def sqrt(x):
        return math.sqrt(x)

    def factorial(n):
        return math.factorial(n)


    def floor(x):
        return math.floor(x)

    def exp(x):
        return math.exp(x)

    def ln(x):
        return math.log(x)

    def binomial(n,p):
        if p<=n :
            
            return div.solve((math.factorial(n),math.factorial(p) * math.factorial(n - p)))
        else :
            return 0
    
    