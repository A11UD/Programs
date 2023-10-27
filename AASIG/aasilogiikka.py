"""
Määrittelee aasigotchin varsinaisen taustalla toimivan logiikan.
"""
import aasimaaritelmat as am

def alusta():
    """
    Alustaa aasidatan, eli luo uuden aasin sekä asettaa sen alkutilanteeseen.
    """
    aasidata = {
        "KYLLÄISYYS": am.ALKU,
        "ONNELLISUUS": am.ALKU,
        "JAKSAMINEN": am.ALKU,
        "IKÄ": 0,
        "RAHA": 0,
        "ELÄKE": False,
    }
    return aasidata

def _vanhene(aasidata):
    """
    Vanhentaa aasia ja jättää sen tarvittaessa eläkkeelle. Tarkoitettu vain
    moduulin sisäiseen käyttöön.
    """
    aasidata["IKÄ"] += 1
    
    if aasidata["IKÄ"] == am.ELAKEIKA:
        aasidata["ELÄKE"] = True

def _tarkista_tilat(aasidata):
    """
    Muuttaa aasin tiloja ajan kuluessa ja jättää aasin tarvittaessa
    sairaseläkkeelle. Tarkoitettu vain moduulin sisäiseen käyttöön.
    """
    if aasidata["IKÄ"] % 2 == 0:
        if aasidata["KYLLÄISYYS"] > 6 and aasidata["JAKSAMINEN"] < am.MAKSIMI_TILA:
            aasidata["JAKSAMINEN"] += 1
        aasidata["KYLLÄISYYS"] -= 1
    if aasidata["IKÄ"] % 3 == 0:
        aasidata["ONNELLISUUS"] -= 1
    
    if aasidata["KYLLÄISYYS"] <= 0 or aasidata["ONNELLISUUS"] <= 0 or aasidata["JAKSAMINEN"] <= 0:
        aasidata["ELÄKE"] = True

def ruoki(aasidata):
    """
    Ruokkii aasia, eli kasvattaa aasin kylläisyyttä, ellei se ole jo maksimissa.
    """
    _vanhene(aasidata)
    _tarkista_tilat(aasidata)
    if aasidata["KYLLÄISYYS"] < am.MAKSIMI_TILA:
        aasidata["KYLLÄISYYS"] += 1
    
def kutita(aasidata):
    """
    Kutittaa aasia, eli kasvattaa aasin onnellisuutta, ellei se ole jo maksimissa.
    """
    _vanhene(aasidata)
    _tarkista_tilat(aasidata)
    if aasidata["ONNELLISUUS"] < am.MAKSIMI_TILA:
        aasidata["ONNELLISUUS"] += 1

def tyoskentele(aasidata):
    """
    Teettää aasilla töitä, eli vähentää aasin jaksamista rahapalkkaa vastaan.
    """
    _vanhene(aasidata)
    aasidata["JAKSAMINEN"] -= 1
    aasidata["RAHA"] += 1
    _tarkista_tilat(aasidata)