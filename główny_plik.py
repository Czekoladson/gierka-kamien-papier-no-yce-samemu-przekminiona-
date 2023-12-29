import sys,random
wyg = 0
rem = 0
por = 0
comruch = "" # ruch komputera
print("WItaj w gre papier kamień nożyce ")
while True:
    print("%s zwycięstw, %s remisów, %s porażek" % (wyg,rem,por)) # wyświetla wynik ogólny
    while True:
        print("Wykonaj ruch: (p)papier,(k)kamień,(n)nożyce,w(wyjście): ")
        ruch = input()
        if ruch == "w": # jak w to wychodzi
            sys.exit()
        if ruch == "k" or ruch == "p" or ruch == "n":
            break
        print("Wpisz litere k , p lub n:")

    if ruch == "k":
        print("Kamień vs...")
    
    elif ruch == "p":
        print("Papier vs...")

    elif ruch == "n":
        print("Nożyce vs...")

    
    rnumer = random.randint(1,3) # generowanie randomowych numerów i zamienianie ich na litery(k,p,n)

    if rnumer == 1: # ruch komputera
        comruch = "k"
        print("Kamień")
    elif rnumer == 2:
        comruch = "p"
        print("Papier")
    elif rnumer == 3:
        comruch = "n"
        print("Nożyce")
    if ruch == comruch:
        print("Remis")
        rem = rem +1

    elif ruch == "k" and comruch == "n": # sytuacje wygrane
        print("wygrałeś")
        wyg = wyg + 1

    elif ruch == "p" and comruch == "k":
        print("Wygrrałeś")
        wyg = wyg + 1
    
    elif ruch == "n" and comruch == "p":
        print("Wygrałeś")
        wyg = wyg + 1


    elif ruch == "k" and comruch == "p": #sytuacje przegrane
        print("Przegrałeś")
        por = por + 1

    elif ruch == "p" and comruch == "n":
        print("Przegrałeś")
        por = por + 1

    elif ruch == "n" and comruch == "k":
        print("Przegrałeś")
        por = por + 1
    