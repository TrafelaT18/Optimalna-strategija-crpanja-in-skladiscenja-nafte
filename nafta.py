from email.charset import QP
import math

# d - dobiček
# X - zaloga na začetku dneva

# K - max izčrpana dnevna količna
# P - cena nafte
# STRc - stroški črpanja nafte
# STRs - stroški shranjevanja nafte
# x - zaloga na koncu dneva

def nafta(dni, K,S, P, STRc, STRs):
    # npr. nafta(10, 3, [10, 20, 30], 40, [5, 10, 7], [3, 4, 9])
    inf = float('inf') # neskončnost
    d = {(0, 0): 0} # slovar optimalnih dobičkov - začnemo brez zaloge in dobička
    p = {(0, 0): None} # slovar parametrov - kako smo prišli do optimalnega dobička
    for i in range(dni): # za vsak dan od 1 naprej
        for x in range(S+1): # končna zaloga dne i
            kandidati = [(-inf, (0, 0, 0))] # seznam dobičkov - začnemo z -inf
            for Qi in range(K+1): # koliko izčrpamo <= K
                for Qp in range(max(0, Qi - x), S + Qi - x + 1): # koliko prodamo >= koliko izčrpamo - končna zaloga = višek, <= kapaciteta + višek
                    x_prev = x + Qp - Qi # zaloga iz prejšnjega dne
                    ix_prev = (i, x_prev) # podatki za prejšnji dan
                    if ix_prev in d: # preverimo, ali imamo podatke za prejšnji dan
                        d_strategije = P[i] * Qp - STRc[i] * Qi - STRs[i] * x 
                        di = P[i] * Qp - STRc[i] * Qi - STRs[i] * x + d[ix_prev] # skupni dobiček
                        kandidati.append((di, (Qi, Qp, x_prev))) # dodamo skupni dobiček in parametre med kandidate
            M, par = max(kandidati) # dobimo maksimalni skupni dobiček
            d[i+1, x] = M # shranimo maksimalni dobiček
            p[i+1, x] = par # shranimo parametre za maksimalni dobiček
            print(d_strategije,par)
    koncna_zaloga = 0
    resitev = {}
    for i in range(dni, 0, -1):
        resitev[i, koncna_zaloga]=p[i, koncna_zaloga]
        koncna_zaloga = p[i, koncna_zaloga][2]
    resitev = dict(list(resitev.items())[::-1])
    return (d[dni, 0], resitev) # optimalni dobiček in parametri za rekonstrukcijo