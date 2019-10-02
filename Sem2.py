import matplotlib.pyplot as plt, random, copy

def oppgave1():
    store_tall = [
        ["Million",    "10^6 ", "10^6 "],
        ["Milliard",   "     ", "10^9 "],
        ["Billion",    "10^9 ", "10^12"],
        ["Billiard",   "     ", "10^15"],
        ["Trillion",   "10^12", "10^18"],
        ["Quadrillion","10^15", "10^24"],
        ["Quintillion","10^18", "10^30"],
        ["Sextillion", "10^21", "10^36"]
    ] 
    print("navn\t\tkort\tlang")
    for row in store_tall:
        for column in row:
            print(column, end=' \t')
        print()


def oppgave2():
    ferdig = False
    tall = []
    print("Skriv inn så mange heltall du vil, og avslutt med 'ferdig ... eller noe som ikke er tall '.")

    while not ferdig:
        inn = input("Tall: ")

        if inn.lower() == "ferdig" or not inn.isdigit():
            ferdig = True
        else:
            tall.append(inn)

    tall.sort()
    length = len(tall)

    if length % 2 == 0:
        a = float(tall[len(tall) // 2])
        b = float(tall[(len(tall) // 2) - 1])
        median = (a+b)/2.0
    else:
        median = float(tall[len(tall)//2])

    print("Medianen av verdiene er: %.2f" % median)


# I billion USD (kort form)
microsoft_inntekt_dollar = [
        [2002, 28.37],
        [2003, 32.19], 
        [2004, 36.84], 
        [2005, 39.79],  
        [2006, 44.28], 
        [2007, 51.12],   
        [2008, 60.42],   
        [2009, 58.44],
        [2010, 62.48],    
        [2011, 69.94],  
        [2012, 73.12],  
        [2013, 77.85],   
        [2014, 86.83],  
        [2015, 93.58],    
        [2016, 85.32],  
        [2017, 89.95],   
        [2018, 110.36],   
        [2019, 125.84]
    ]


def oppgave3a():
    USD = 8.6862
    microsoft_inntekt_kroner = copy.deepcopy(microsoft_inntekt_dollar)

    for row in microsoft_inntekt_kroner:
        row[1] = row[1]*USD
        for column in row:
            print(column, end=' \t')
        print()

    print("\nOld: ")
    for row in microsoft_inntekt_dollar:
        for column in row:
            print(column, end=' \t')
        print()


def oppgave3b():
    år = []
    inntekt = []
    for row in microsoft_inntekt_dollar:
        år.append(row[0])
        inntekt.append(row[1])

    plt.bar(år,inntekt)
    plt.ylabel("Earnings in Billion USD")
    plt.xlabel("Year")
    plt.show()


def oppgave3c():
    inntekt = 0
    for row in microsoft_inntekt_dollar:
        inntekt += row[1]
    print("Mirosoft tjente %.2f billioner dollar i perioden 2002-2019" % (inntekt*1000))


def print_kart(kart):  
    for rad in kart:      
       print("".join(rad))

def oppdater_kart(spillerX, spillerY, monsterX, monsterY):    ''' Printer et 10 * 10 kart med spiller i posisjon (spillerX, spillerY)    og monster i posisjon (monsterX, monsterY)    
    input:
        spillerX og spillerY, heltall mellom 0 og 9
    return: 
           None
     '''    
   # kart = []    
    # Lag kart her ->    
   # print_kart(kart)
pass
     
def flytt_spiller(bevegelse, spillerX, spillerY):    ''' Flytt spiller hvis lovlig trekk    
    input:        bevegelse: w,a,s,d
                    spillerX og spillerY, heltall mellom 0 og 9
    return:        spillerX, spillerY, heltall mellom 0 og 9    '''    
pass

def oppgave4():
    map = ["*"]*10


   # print_kart(map)
  #  playing = True
  #  while playing:



oppgave4()
"""while True:
    valg = input("\n\033[4mHvilke oppgave?\033[0m \t 1, 2, 3a, 3b, 3c, 4 eller Alle? \033[m \t \033[4m Avslutt: 0 \033[m \n").upper()
    if valg == "1":
        oppgave1()
    elif valg == "2":
        oppgave2()
    elif valg == "3A":
        oppgave3a()
    elif valg == "3B":
        oppgave3b()
    elif valg == "3C":
        oppgave3c()
    elif valg == "4":
        oppgave4()
    elif valg == "0":
        break
    elif valg == "ALLE":
        oppgave1()
        oppgave2()
        oppgave3a()
        oppgave3b()
        oppgave3c()
        oppgave4()
    else:
        print("Ugylidg, prøv igjen.")

        """