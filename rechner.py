def potenz(task):
    amount = task.count("^")
    for i in range(amount):
        pos = task.rfind("^")

        # a bestimmen
        start=pos-1
        while start >=0 and task[start] in ".0123456789":
            start-=1

        if task[start+1:pos] in ".":
            a = float(task[start+1:pos])
        else:
            a = int(task[start+1:pos])

        # b bestimmen
        end = pos+1
        while end < len(task) and task[end] in ".0123456789":
            end+=1
        b = float(task[pos+1:end])
        if str(b)[-2:]==".0":
            b=int(b)

        ergebnis = a ** b

        if str(ergebnis)[-2:]==".0":
            ergebnis=int(ergebnis)

        #print(f"a:{a} b:{b}")
        print(f"Jetzt: {a}^{b}={ergebnis}")
        task = task.replace(task[start+1:end], str(ergebnis), 1)
        print(task)
    return task
        


def multiplikation(task):
    amount = task.count("*")
    for i in range(amount):
        pos = task.find("*")
        operator = task[pos]

        # a bestimmen
        start=pos-1
        while start >=0 and task[start] in ".0123456789":
            start-=1
        a = float(task[start+1:pos])
        if str(a)[-2:]==".0":
            a=int(a)

        # b bestimmen
        end = pos+1
        while end < len(task) and task[end] in ".0123456789":
            end+=1
        b = float(task[pos+1:end])
        if str(b)[-2:]==".0":
            b=int(b)

        ergebnis = a*b

        if str(ergebnis)[-2:]==".0":
            ergebnis=int(ergebnis)

        #print(f"a:{a} b:{b}")
        print(f"Jetzt: {a}{operator}{b}={ergebnis}")
        task = task.replace(task[start+1:end], str(ergebnis), 1)
        print(task)
    return task


def division(task):
    amount = task.count("/")
    for i in range(amount):
        pos = task.find("/")

        # a bestimmen
        start=pos-1
        while start >=0 and task[start] in ".0123456789":
            start-=1
        a = float(task[start+1:pos])
        if str(a)[-2:]==".0":
            a=int(a)

        # b bestimmen
        end = pos+1
        while end < len(task) and task[end] in ".0123456789":
            end+=1
        b = float(task[pos+1:end])
        if str(b)[-2:]==".0":
            b=int(b)

        ergebnis = a/b

        if str(ergebnis)[-2:]==".0":
            ergebnis=int(ergebnis)

        #print(f"a:{a} b:{b}")
        print(f"Jetzt: {a}/{b}={ergebnis}")
        task = task.replace(task[start+1:end], str(ergebnis), 1)
        print(task)
    return task


def strich(task):
    amount = task.count("+")
    amount += task.count("-")
    for i in range(amount):
        posp = task.find("+")
        posm = task.find("-")
        if posm == -1:
            pos = posp
        elif posp == -1:
            pos= posm
        else:
            pos = min(posp, posm)

        operator = task[pos]

        # a bestimmen
        start=pos-1
        while start >=0 and task[start] in ".0123456789":
            start-=1
        a = float(task[start+1:pos])
        if str(a)[-2:]==".0":
            a=int(a)

        # b bestimmen
        end = pos+1
        while end < len(task) and task[end] in ".0123456789":
            end+=1
        b = float(task[pos+1:end])
        if str(b)[-2:]==".0":
            b=int(b)

        if task[pos]=="+":       
            ergebnis = a + b
        else:
            ergebnis = a-b

        if str(ergebnis)[-2:]==".0":
            ergebnis=int(ergebnis)

        #print(f"a:{a} b:{b}")
        print(f"Jetzt: {a}{operator}{b}={ergebnis}")
        task = task.replace(task[start+1:end], str(ergebnis), 1)
        print(task)
    return task
