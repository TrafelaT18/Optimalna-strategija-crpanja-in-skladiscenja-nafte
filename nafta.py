from email.charset import QP
import math

def nafta(dni, K,S, P, STRc, STRs):
    # npr. nafta(3, 10, 40,[10, 20, 30], [5, 10, 7], [3, 4, 9])
    inf = float('inf') # neskončnost
    d = {(0, 0): 0} # slovar potencialnih optimalnih dobičkov 
    p = {(0, 0): None} # slovar parametrov 
    for i in range(dni): # za vsak dan od 1 naprej
        for x in range(S+1): # končna zaloga dne i
            kandidati = [(-inf, (0, 0, 0,0))] # seznam dobičkov 
            for Qi in range(K+1): # koliko izčrpamo <= K
                for Qp in range(max(0, Qi - x), S + Qi - x + 1):# višek če ni začetne zaloge<=koliko prodamo<=višek če je polna začetna zaloga(kapaciteta+višek)
                    x_vceraj = x + Qp - Qi # zaloga iz prejšnjega dne oz. začetna zaloga tega dne
                    ix_vceraj = (i, x_vceraj) # podatki za prejšnji dan
                    if ix_vceraj in d: # preverimo, ali imamo podatke prejšnjega dne
                        d_strategije = P[i] * Qp - STRc[i] * Qi - STRs[i] * x  #dnevni dobiček
                        di = d_strategije + d[ix_vceraj] # skupni dobiček
                        kandidati.append((di, (d_strategije, Qi, Qp, x_vceraj))) # dodamo skupni dobiček, dnevni dobiček in parametre med kandidate
            M, strategija = max(kandidati) # dobimo maksimalni skupni dobiček
            d[i+1, x] = M # shranimo maksimalni dobiček
            p[i+1, x] = strategija # shranimo parametre za maksimalni dobiček
    koncna_zaloga = 0
    resitev = {}
    for i in range(dni, 0, -1): #izberemo optimalno strategijo za dobiček
        resitev[i, koncna_zaloga]=p[i, koncna_zaloga]
        koncna_zaloga = p[i, koncna_zaloga][3]
    resitev = dict(list(resitev.items())[::-1])
    return (d[dni, 0], resitev) # optimalni dobiček in parametri za rekonstrukcijo, d[dni, 0], resitev

