import aasilogiikka
import aasimaaritelmat as am
import aasikaytto

def main():
    aasidata = aasilogiikka.alusta()
    
    while True:
        aasikaytto.nayta_tila(aasidata)
        syote = aasikaytto.pyyda_syote(aasidata)
        
        if syote == am.LOPETA:
            break
        elif syote == am.RUOKI:
            aasilogiikka.ruoki(aasidata)
        elif syote == am.KUTITA:
            aasilogiikka.kutita(aasidata)
        elif syote == am.TYOSKENTELE:
            aasilogiikka.tyoskentele(aasidata)
        elif syote == am.ALUSTA:
            aasidata = aasilogiikka.alusta()
    return aasidata
if __name__ == "__main__":
    main()