from email.charset import QP
import math

# d - dobiček
# X - zaloga na začetku dneva
# K - max izčrpana dnevna količna
# P - cena nafte
# STRc - stroški črpanja nafte
# STRs - stroški shranjevanja nafte

def nafta(K, dni, P, S, STRc, STRs):
    def nafta(K, dni, P, S, STRc, STRs):
    # npr. nafta(10, 3, 30, 40, [5, 10, 7],[13, 14, 9])
    koncni_rezultati = {}
    dnevni_rezultati = {}
    dobicki_v_dnevu = []
    X = 0
    d = 0
    for i in range(dni): #za vsak dan
        for Qi in range(K+1): #Koliko izčrpamo<=K
            for Qp in range(Qi+X+1): #koliko prodamo <= koliko izčrpam + začetna zaloga
                for x in range(S+1): # x optimalna zaloga 
                    if x == X +Qi-Qp: 
                        di=P*Qp-Qi*STRc[i]-STRs[i]*x #dobiček
                        dnevni_rezultati[di] = (Qi, Qp, x) #dodajava v slovar dobiček in količino Qi in Qp
                        dobicki_v_dnevu += [di] #dodajava v seznam
                    else:
                        pass
        M = max(dobicki_v_dnevu)
        par = dnevni_rezultati[M]
        X = x
        d += M 
        koncni_rezultati[M] = dnevni_rezultati.get(M)
        dobicki_v_dnevu = []         
        dnevni_rezultati = {}
    return koncni_rezultati

