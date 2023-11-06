from datetime import datetime
from tkinter import *
import tkinter.font
import json


tapahtumalista = []


tapahtuma = {
"nimi" : "x",
"alku" : "x",
"kesto" : "x"
}


valinnat = ["L", "P", "T"]


#Kysytään tapahtuman tiedot ja lisätään se muistiin
def lisaa_tapahtuma():
    tapahtuma_nimi = input("Tapahtuma nimi : ")
    while True:
        try:
            tapahtuma_alku = input("Tapahtuman alkamisaika muodossa YYYY-MM-DD HH:MM:SS : ")
            tapahtuma_date = datetime.strptime(tapahtuma_alku, '%Y-%m-%d %H:%M:%S')
            break

        except ValueError:
            print("Anna alkamisaika käsketyssä muodossa!")

    tapahtuma_kesto = input("Tapahtuman kesto muodossa HH:MM:SS : ")
    tapahtuma["nimi"] = tapahtuma_nimi 
    tapahtuma["alku"] = tapahtuma_date 
    tapahtuma["kesto"] = tapahtuma_kesto
    kopio = dict(tapahtuma)
    tapahtumalista.append(kopio)
    return


#Kysytään poistettavan tapahtuman nimi ja tuhotaan se
def poista_tapahtuma():
    poistettava_tapahtuma = input("Syötä poistettavan tapahtuman nimi tai poistu näppäimellä q : ")
    for i in range(len(tapahtumalista)):
        if tapahtumalista[i]['nimi'] == poistettava_tapahtuma:
            del tapahtumalista[i]
            break
        elif poistettava_tapahtuma == "q":
            break
        else:
           print("Ei ole tällaista tapahtumaa")
    return


#tulostaa kalenterin
def tulosta_kalenteri():       


        sorted_list = sorted(tapahtumalista, key=lambda x: x['alku'])
        syote1, syote2 = input('''Mikäli et halua määritellä aikaväliä kirjoita (,) 
        Pvm asti kirjoita (YYYY-MM-DD) (, Loppu)
        Pvm alkaen kirjoita (YYYY-MM-DD) (Alku,)                 
        Aikaväli päivämääränä (YYYY-MM-DD) (Alku , Loppu) : ''').split(",")
        if syote1 == "" and syote2 == "":
         for idx, tapahtuma in enumerate(sorted_list):
            print(f"Tapahtuma {tapahtuma['nimi']} alkaa {tapahtuma['alku']} ja tapahtuma kestää {tapahtuma['kesto']}")
        

        elif syote2 == "":
         aikavali1 = datetime.strptime(syote1.strip(), '%Y-%m-%d')
         for idx, tapahtuma in enumerate(sorted_list):
           if tapahtuma["alku"] > aikavali1:
            print(f"Tapahtuma {tapahtuma['nimi']} alkaa {tapahtuma['alku']} ja tapahtuma kestää {tapahtuma['kesto']}")


        elif syote1 == "":
         aikavali2 = datetime.strptime(syote2.strip(), '%Y-%m-%d')
         for idx, tapahtuma in enumerate(sorted_list):
           if tapahtuma["alku"] < aikavali2:
            print(f"Tapahtuma {tapahtuma['nimi']} alkaa {tapahtuma['alku']} ja tapahtuma kestää {tapahtuma['kesto']}")


        else:
            aikavali1 = datetime.strptime(syote1.strip(), '%Y-%m-%d')
            aikavali2 = datetime.strptime(syote2.strip(), '%Y-%m-%d')
            for idx, tapahtuma in enumerate(sorted_list):
                if tapahtuma["alku"] > aikavali1 and tapahtuma["alku"] < aikavali2:
                    print(f"Tapahtuma {tapahtuma['nimi']} alkaa {tapahtuma['alku']} ja tapahtuma kestää {tapahtuma['kesto']}")


#Piirtää kalenterin Tkinterin avulla
def piirra_kalenteri():
    window = Tk("Kalenteri")
    sorted_list = sorted(tapahtumalista, key=lambda x: x['alku'])
    for idx, tapahtuma in enumerate(sorted_list):
        teksti = (f"Tapahtuma {tapahtuma['nimi']} alkaa {tapahtuma['alku']} ja tapahtuma kestää {tapahtuma['kesto']}")
        label = Label(text=teksti, width = 80, fg="white", bg="black", font =('Jokerman', 24))
        label.pack()
    btn = Button(window, text ="Palaa", command = window.destroy)
    btn.pack(side = 'top')
    window.mainloop()
    

def tallenna_tiedot():
   for i in range(len(tapahtumalista)):
    tapahtumalista[i]["alku"] = datetime.strftime(tapahtumalista[i]["alku"],'%Y-%m-%d %H:%M:%S')
   with open("tapahtumat.json", "w", encoding="utf-8") as write_file: 
    json.dump(tapahtumalista, write_file, indent=4)   


def tuo_tiedot():
    with open("tapahtumat.json", "r", encoding="utf-8") as read_file:
        tapahtumalista = json.load(read_file)
    for i in range(len(tapahtumalista)):
        tapahtumalista[i]["alku"] = datetime.strptime(tapahtumalista[i]["alku"],'%Y-%m-%d %H:%M:%S') 
    return tapahtumalista
print(tapahtumalista)


def kysy_toimintoa():
    while True:
        print('''Mahdollisia toimintoja ovat
    Lisaa tapahtuma (L)
    Poista tapahtuma (P)
    Tulosta kalenteri (T)
    Piirrä kalenteri (K)
    Tallensa tiedot tiedostoon(s)
    Tuo tiedot tiedostosta(i)
    Lopeta toiminta (Q)''')
        valinta = input("Tee valintasi :").lower()
        if valinta == "l":
            print("Lisätään tapahtuma")
            lisaa_tapahtuma()
        elif valinta == "p":
            print("Poistetaan tapahtuma")
            poista_tapahtuma()
        elif valinta == "t":
            print("Tulostetaan kalenteri")
            tulosta_kalenteri()
        elif valinta == "k":
            print("Piirretään kalenteri")
            piirra_kalenteri()
        elif valinta == "s":
            print("Tallennetaan tiedot")
            tallenna_tiedot()
        elif valinta == "i":
            print("Tuodaan tiedot")
            tuo_tiedot()
        elif valinta == "q":
            print("Lopetetaan...")
            break
        else : 
            print("Väärä valinta, kokeile uudestaan")
    return




kysy_toimintoa()
