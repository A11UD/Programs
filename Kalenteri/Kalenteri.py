"""
Kalenteri - yksinkertainen terminaali Kalenteri.

@author: Aleksanteri Aska, student, Oulun yliopisto 2023

"""



from datetime import datetime
from tkinter import *
import json




tapahtumalista = []


tapahtuma = {
"nimi" : "x",
"alku" : "x",
"kesto" : "x"
}




def lisaa_tapahtuma():
    '''
    Kysytään tapahtuman tiedot ja lisätään se muistiin
    '''
    tapahtuma_nimi = input("Tapahtuma nimi : ")
    while True:
        try:
            tapahtuma_alku = input("Tapahtuman alkamisaika muodossa YYYY-MM-DD HH:MM:SS : ")
            tapahtuma_date = datetime.strptime(tapahtuma_alku, '%Y-%m-%d %H:%M:%S')
            break
        except ValueError:
            print("Anna alkamisaika käsketyssä muodossa!")
    tapahtuma_kesto = input("Tapahtuma kesto muodossa HH:MM:SS : ")
    tapahtuma["nimi"] = tapahtuma_nimi 
    tapahtuma["alku"] = tapahtuma_date 
    tapahtuma["kesto"] = tapahtuma_kesto
    kopio = dict(tapahtuma)
    tapahtumalista.append(kopio)


def poista_tapahtuma():
    '''
    Kysytään poistettavan tapahtuman nimi ja tuhotaan se
    '''
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




def piirra_kalenteri():
    '''
    Piirtää kalenterin Tkinterin avulla
    '''
    window = Tk("Kalenteri")
    sorted_list = sorted(tapahtumalista, key=lambda x: x['alku'])
    for tapahtuma in sorted_list:
        teksti = (f"Tapahtuma {tapahtuma['nimi']} alkaa {tapahtuma['alku']} ja tapahtuma kestää {tapahtuma['kesto']}")
        label = Label(text=teksti, width = 80, fg="white", bg="black", font =('Jokerman', 24))
        label.pack()
    btn = Button(window, text ="Palaa", command = window.destroy)
    btn.pack(side = 'top')
    window.mainloop()
    

def tallenna_tiedot():
    '''
    Kysyy tiedoston nimen ja tallentaan annettuun tiedostoon
    '''
    for i in range(len(tapahtumalista)):
        tapahtumalista[i]["alku"] = datetime.strftime(tapahtumalista[i]["alku"],'%Y-%m-%d %H:%M:%S')
    fileName = input("Anna halutun Json tiedoston nimi ilman .json: ")
    with open(f"{fileName}.json", "w", encoding="utf-8") as write_file: 
        json.dump(tapahtumalista, write_file, indent=4)   
    for i in range(len(tapahtumalista)):
        tapahtumalista[i]["alku"] = datetime.strptime(tapahtumalista[i]["alku"],'%Y-%m-%d %H:%M:%S') 

def tuo_tiedot():
    '''
    Kysyy tiedoston nimen ja tuo sielta tiedot
    '''
    fileName2 = input("Anna halutun Json tiedoston nimi ilman .json: ")
    with open(f"{fileName2}.json", "r", encoding="utf-8") as read_file:
        kopio2 = json.load(read_file)
    for i in range(len(kopio2)):
        kopio2[i]["alku"] = datetime.strptime(kopio2[i]["alku"],'%Y-%m-%d %H:%M:%S') 
    tapahtumalista.extend(kopio2)


def tulosta_kalenteri():
    '''
    Tulostaa kalenterin, kysyy aikavalin ja tulostaa halutun aikavalin.
    '''
    sorted_list = sorted(tapahtumalista, key=lambda x: x['alku'])
    while True:
        try:
            syote1, syote2 = input('''Mikäli et halua määritellä aikaväliä kirjoita (,) 
            Pvm asti kirjoita (YYYY-MM-DD) (, Loppu)
            Pvm alkaen kirjoita (YYYY-MM-DD) (Alku,)                 
            Aikaväli päivämääränä (YYYY-MM-DD) (Alku , Loppu) : ''').split(",")
            break
        except ValueError:
            print("Väärin meni, Seurasitko ohjeita?")
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


def kysy_toimintoa():
    '''
    Kysyy käyttäjältä toimintoa ja kutsuu tarvittavan funktion
    '''
    while True:
        print('''Mahdollisia toimintoja ovat
    Lisaa tapahtuma (L)
    Poista tapahtuma (P)
    Tulosta kalenteri (T)
    Piirrä kalenteri (K)
    Tallenna tiedot tiedostoon(s)
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
