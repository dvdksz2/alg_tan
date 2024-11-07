#!/bin/python3

# beolvassuk a sorozat elemeit
sorozat = list(map(int, input().split(" ")))

# ebben a listaban fogjuk tarolni a sorozat elemeit
sor = []

# ebben a listaban fogjuk tarolni a kiirt szamokat
# a kiiras sorrendjeben
kimenet = []

# format sztring a kiiras megkonnyitesehez
aktualis_allapot = "{}. sor = {}, kimenet = {}"

# ciklusszamlalo
szamlalo = 0
for szam in sorozat:
    szamlalo += 1

    # ha a sor ures, a vegere tesszuk az aktualis szamot
    if not sor:
        sor.append(szam)

    # ha a sor utolsojanal nagyobb az aktualis szam, akkor
    # az aktualis szamot a sor vegere tesszuk
    elif sor[-1] < szam:
        sor.append(szam)

    # ha az utolso kiirtnál kisebb az aktualis szam, akkor
    # hibajelzessel megallunk
    elif kimenet and szam < kimenet[-1]:
        print("HIBA: Utolso kiirtnal kisebb szam.")
        exit()

    # ha a sor elsojenel kisebb az aktualis szam, akkor
    # kiirjuk az aktualis szamot
    elif szam < sor[0]:
        kimenet.append(szam)
    else:
        # amig a sor elsojenel nagyobb az aktualis szam, addig
        # kiirjuk a sor elsojet (es a kiirt elemet ki is vesszuk a sorbol);
        # ilyenkor, ha a sor uresse valik, akkor a bemeneti erteket
        # a sorba tesszuk, kulonben kiirjuk
        while sor and sor[0] < szam:
            kimenet.append(sor[0])
            del sor[0]
        if not sor:
            sor.append(szam)
        else:
            kimenet.append(szam)

    # minden elem erkezése utan megadjuk a sorban levo elemeket
    # es a kiirt ertekeket
    print(aktualis_allapot.format(szamlalo, sor, kimenet))

szamlalo += 1

# az utolso ertek feldolgozasa utan a sorban levo elemeket kiirjuk
while sor:
    kimenet.append(sor[0])
    del sor[0]

print(aktualis_allapot.format(szamlalo, sor, kimenet))
