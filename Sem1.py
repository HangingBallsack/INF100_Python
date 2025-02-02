# Oppg 1
def func1():
    print("\n-------------Oppgave 1-------------")

    while True:
        try:
            x = float(input("Tall nr 1: "))
            y = float(input("Tall nr 2: "))
            z = float(input("Tall nr 3: "))
        except ValueError:
            print("------ Tall =/= bokstav ------ \n")
            continue
        else:
            break

    text = "Disse tallene er "
    if x < y < z:
        print(text + "stigende")
    elif x > y > z:
        print(text + "synkende")
    else:
        print(text + "ingen av delene")


# Oppg 2a
def func2():
    print("\n-------------Oppgave 2-------------")

    D = "Ruter"
    H = "Hjerter"
    S = "Spar"
    C = "Kløver"

    bokstav = str(input("Skriv en av disse: D, H, S eller C\n"))
    if bokstav.upper() == "D":
        print(D)
    elif bokstav.upper() == "H":
        print(H)
    elif bokstav.upper() == "S":
        print(S)
    elif bokstav.upper() == "C":
        print(C)
    else:
        print("--------ugyldig innput--------")
        return

# Oppg 2b
    kortStokk = {
        "A": "Ess",
        "J": "Knekt",
        "Q": "Dame",
        "K": "Konge",
        "2": "To",
        "3": "Tre",
        "4": "Fire",
        "5": "Fem",
        "6": "Seks",
        "7": "Syv",
        "8": "Åtte",
        "9": "Ni",
        "10": "Ti"
    }
    kort = input("\nTall: 2 - 10 \t eller \t A, J, Q, K\n")
    print(kortStokk[kort.upper()])


# oppg 3
def func3():
    print("\n-------------Oppgave 3-------------")

    ValutaKurser = {
        "EUR": 9.68551,
        "USD": 8.50373,
        "GBP": 11.0134,
        "SEK": 0.92950,
        "AUD": 6.06501,
        "NOK": 1.00000
    }
    kursFra = input("Fra hvilke valuta vil du konvertere? EUR, USD, GBP, SEK, AUD \n").upper()
    kursFraAntall = float(input("Hvor mange %s vil du konvertere til NOK?\n" % (kursFra)))

    konvertert = kursFraAntall * ValutaKurser[kursFra.upper()]
    print("%.1f %s er %.2f i NOK." % (kursFraAntall, kursFra, konvertert))

    konvFraNorsk = float(input("\nNorske kroner som skal konverteres: "))
    konvFraNorskTil = input("Til hvilke kurs?  EUR, USD, GBP, SEK, AUD\n").upper()
    print("%.1f Norske er %.2f %s" % (konvFraNorsk, (konvFraNorsk / ValutaKurser[konvFraNorskTil]), konvFraNorskTil))


# oppg 4
def func4():
    print("\n-------------Oppgave 4-------------")

    for i in range(10):
        print("%d oppøyd i 3: %d" % (i, i**3))


# oppg 5
def func5():
    print("\n-------------Oppgave 5-------------")

    start = int(input("Start: "))
    stopp = int(input("Stopp (til og med): "))
    n = int(input("n: "))

    print("Tall mellom %d og %d som er delelig på %d: " % (start, stopp, n))
    for i in range(start, stopp+1):
        if (i % n == 0):
            print(i)


# oppg 6
def func6():
    print("\n-------------Oppgave 6-------------")

    print("\033[4m Celsius \t Fahrenheit \t\t Status \033[m")
    for i in range(11):
        if i < 6:
            print("%d \t\t %.1f \t\t Jeg har det bra." % ((i*10), tilFahrenheit(i*10)))
        else:
            print("%d \t\t %.1f \t\t Jeg svetter ihjel!" % ((i*10), tilFahrenheit(i*10)))

# tøysete metode som står i oppgaven skal være med :PpPp
def tilFahrenheit(celcius):
    return celcius*1.8+32


# oppg 7
def func7():
    print("\n-------------Oppgave 7-------------")
    verdi = float(input("original pris: "))
    fra = int(input("Fra: "))
    til = int(input("Til: "))
    print(renteOkning(verdi, fra, til))

# tøysete metode som står i oppgaven skal være med :PpPp
def renteOkning(verdi, fra, til):
    for i in range(til-fra):
        verdi *= 1.02
    return verdi


# velg hvilke oppgave som skal vises i terminalen
while True:
    valg = input("\nHvilke oppgave? \t \033[4m 1-7 \033[0m \t \033[4m Alle \033[m \t \033[4m Avslutt: 0 \033[m \n").upper()
    if valg == "1":
        func1()
    elif valg == "2":
        func2()
    elif valg == "3":
        func3()
    elif valg == "4":
        func4()
    elif valg == "5":
        func5()
    elif valg == "6":
        func6()
    elif valg == "7":
        func7()
    elif valg == "0":
        break
    elif valg == "ALLE":
        func1()
        func2()
        func3()
        func4()
        func5()
        func6()
        func7()
    else:
        print("Ugylidg, prøv igjen.")
