x = [1]
class Pascal():


    def run(limit):
        try:
            limit = int(limit)
        except ValueError or TypeError:
            raise ValueError('Pascal line number must be integer')
        if limit > 2:
            triangle = "1"
            for i in range(2, limit + 1):
                y = [x[j-1] + x[j] for j in range(1, i-1)]
                z = y 
                y = [1]
                for k in z:
                    y.append(k)
                y.append(1)
                triangle = triangle +"\n" + " ".join((str(i) for i in y))
                x = y
        elif limit == 1:
            triangle = "1"
        elif limit == 2:
            triangle = "1\n1 1"
        return triangle

    def coef(limit):
        try:
            limit = int(limit)
        except ValueError or TypeError:
            raise ValueError('Pascal line number must be integer')
        if limit > 2:
            line = "1"
            for i in range(2, limit + 1):
                y = [x[j-1] + x[j] for j in range(1, i-1)]
                z = y 
                y = [1]
                for k in z:
                    y.append(k)
                y.append(1)
                x = y
            line = " ".join((str(i) for i in y))
        elif limit == 1:
            line = "1"
        elif limit == 2:
            line = "1\n1 1"
        return line

for i in range(3):
    print(Pascal.coef(input()))