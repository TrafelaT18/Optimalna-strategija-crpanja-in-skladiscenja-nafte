from email.charset import QP




def nafta(d, X, K, dni, P, S):
    #(nafta(0, 0, 50, 5, 4, 200))
    rezultati = {}
    dnevni_rezultati = {}
    STRc=[1, 1, 1.4, 2, 2]
    STRs=[1, 1.5, 1.4, 1, 2]
    dobicki_v_dnevu = [] 
    for i in range(dni): #za vsak dan
        if i == 0:
            rezultati[0] = (0,0)
        for Qi in range(K): #Koliko izčrpam<=K
            for Qp in range(Qi+X): #koliko prodam <= koliko izčrpam+ začetna zaloga
                while X+Qi-Qp <= S:
                    di=P*Qp-Qi*STRc[i]-STRs[i]*(X+Qi-Qp)
                    dnevni_rezultati[di] = (Qi, Qp) #dodajava v slovar
                    dobicki_v_dnevu += [di] #dodajava v seznam
                    M = max(dobicki_v_dnevu)
                    par = dnevni_rezultati[M]
        d += M 
        rezultati[M] = dnevni_rezultati.get(M)
    
    #od določenega key-a želiva dobiti pripadajoči
    # value in dodati v slovar rezultati 
    #X += Qi - Qp ... zaloga na koncu dneva
        X += par[0] - par[1]



        dobicki_v_dnevu = []         
        dnevni_rezultati = {}
    return(rezultati)
