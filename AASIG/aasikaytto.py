import aasimaaritelmat as am
import aasilogiikka as al
aasidata = al.alusta()

def nayta_tila(aasidata):
    """Määrittelee aasigotchin käyttöliittymän toiminnot."""
    print(f"Aasi on {aasidata['IKÄ']} vuotta vanha ja rahaa on {aasidata['RAHA']} mk.")
    print(f"Kylläisyys : {aasidata['KYLLÄISYYS']}")
    print(f"Onnellisuus: {aasidata['ONNELLISUUS']}")
    print(f"Jaksaminen: {aasidata['JAKSAMINEN']}")
    if {aasidata['ELÄKE']} == True:
        print("Aasi on jäänyt eläkkeelle.")
    else:
        pass

def pyyda_syote(aasidata):
    """Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja kysyy uutta
syötettä kunnes käyttäjä antaa laillisen syötteen. Saatu syöte palautetaan."""
    if {aasidata['ELÄKE']} == True:
        #print(f"{nayta_tila(aasidata)}")
        print(f"{am.ELAKEVALINNAT}")
    else: 
       # print((f"{nayta_tila(aasidata)}"))
        print(f"Valinnat : {am.VALINNAT}")
    while True:
        val = input("Anna seuraava valinta :")
        if val != (am.ELAKEVALINNAT) and {aasidata['ELÄKE']} == True:
            print("Virheellinen syöte!")
        if val != "q" and  val != "r" and val != "k" and  val != "t" :
            print("Virheellinen syöte!")
        elif val == "q":   
            return am.LOPETA
        elif val == "r":
            return am.RUOKI
        elif val == "k":
            return am.KUTITA
        elif val == "a":
            am.ALUSTA
        else : 
            return am.TYOSKENTELE
