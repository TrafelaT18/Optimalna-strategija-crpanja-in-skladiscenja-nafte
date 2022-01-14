from email.charset import QP
import math

# d - dobiček
# X - trenutna zaloga
# K - max izčrpana dnevna količna
# P - cena nafte
# STRc - stroški črpanja nafte
# STRs - stroški shranjevanja nafte

def nafta(d, X, K, dni, P, S, STRc, STRs):
    # npr. nafta(0, 0, 50, 5, 6, 200, [1, 2, 4, 1, 2],[1, 1, 6, 2, 3])
    koncni_rezultati = {}
    dnevni_rezultati = {}
    dobicki_v_dnevu = [] 
    for i in range(dni): #za vsak dan
        if i == 0:
            končni_rezultati[0] = (0,0)
        for Qi in range(K): #Koliko izčrpamo<=K
            for Qp in range(Qi+X): #koliko prodamo <= koliko izčrpam + začetna zaloga
                if X+Qi-Qp <= S: 
                    di=P*Qp-Qi*STRc[i]-STRs[i]*(X+Qi-Qp) #dobiček
                    dnevni_rezultati[di] = (Qi, Qp) #dodajava v slovar dobiček in količino Qi in Qp
                    dobicki_v_dnevu += [di] #dodajava v seznam
                else:
                    pass
        M = max(dobicki_v_dnevu)
        par = dnevni_rezultati[M]
        d += M 
        koncni_rezultati[M] = dnevni_rezultati.get(M)
        X += par[0] - par[1]  #X += Qi - Qp ... zaloga na koncu dneva
        dobicki_v_dnevu = []         
        dnevni_rezultati = {}
    return koncni_rezultati
