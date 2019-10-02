import matplotlib.pyplot as plt
import random

def oppgave1():    """ Printer ut store tall i kort og lang form,        ofte kalt amerikansk og britisk form.    """    
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
pass

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

def oppgave2():    """ Henter en rekke tall fra brukeren og ut hva som         var medianen i listen    """    
pass

def oppgave3a():    """ Konverterer inntektene fra dollar til kroner    uten Ã¥ gjÃ ̧re endringer pÃ¥ originallisten.    """    
pass

def oppgave3b():    """ Tegner et histogram over inntektene til Microsoft    """    
pass

def oppgave3c():    """ Summerer opp inntektene til Microsoft    """    
pass

def print_kart(kart):  
    for rad in kart:      
        print("".join(rad))

        ''' Printer et 10 * 10 kart per rad   
    input:       kart, en list
      return:      
      None'''  
          
def oppdater_kart(spillerX, spillerY, monsterX, monsterY):    ''' Printer et 10 * 10 kart med spiller i posisjon (spillerX, spillerY)    og monster i posisjon (monsterX, monsterY)    
    input:
        spillerX og spillerY, heltall mellom 0 og 9
    return: 
           None
     '''    
    kart = []    
    # Lag kart her ->    
    print_kart(kart)
     
def flytt_spiller(bevegelse, spillerX, spillerY):    ''' Flytt spiller hvis lovlig trekk    
    input:        bevegelse: w,a,s,d
                    spillerX og spillerY, heltall mellom 0 og 9
    return:        spillerX, spillerY, heltall mellom 0 og 9    '''    
pass

def oppgave4():    ''' Spill mot monster'''   
pass

def main():    
    # oppgave1()    
    # # print()    
    # # oppgave2a()    
    # # print()    
    # # print()    
    # # oppgave3a()    
    # # print()    
    # # oppgave3b()    
    # # print()    
    # # oppgave3c()    
    # # print()
    # # oppgave4c()    
    # # print()