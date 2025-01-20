import rechner

def hauptprogramm(task):

    # Potenz
    if "^" in task:
        try:
            task=rechner.potenz(task)
        except ValueError:
            print("Zahl zu groß")
            

    # Punkt
    if "*" in task:
        task=rechner.multiplikation(task)


    if "/" in task:
        try:
            task=rechner.division(task)
                
        except ZeroDivisionError:
            print("nicht durch 0 teilbar")


    # Strich
    if "+" in task or "-" in task:
        task=rechner.strich(task)

    
    #task = input("Deine Aufgabe ")
    #task = task.replace(" ", "")
    return task


name = input("Hallo, ich bin der Taschenrechner 2000. Wie heißen Sie? ")
print(f'Hallo {name.capitalize()}! :)\nZum Beenden einfach "esc" schreiben')

while True:
    task = input("Deine Aufgabe ")
    task = task.replace(" ", "")

    # Rechner beenden
    if task == "esc":   
        print("Bis bald! :)")
        break

    # Klammer
    while "(" in task:
        amount_open=task.count("(")
        amount_close=task.count(")")
        if amount_open==amount_close:
            pos_openbracket = task.find("(")
            pos_closingbracket = task.find(")")
            bracket = task[pos_openbracket+1:pos_closingbracket]

            print("Klammer: "+ bracket) #prüfung

            ergebnis=hauptprogramm(bracket)

            task = task.replace(task[pos_openbracket:pos_closingbracket+1], str(ergebnis), 1)

            print(task)
        else:
            print("Klammer fehlt")

    ergebnis = hauptprogramm(task)
    print("------------------------------")
