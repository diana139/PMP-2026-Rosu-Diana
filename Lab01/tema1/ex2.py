import random
import numpy as np
import matplotlib.pyplot as plt

#a)
# P(stema) = 1/2
# P(ban ) = 1/2
# jocul se termina cand se obtine stema, adica p(stema) = 1/2
# deci  urmează o distribuție geometrică de parametru p = 1/2


#A -- 1 jucator
#B --al2 lea jucator

def joc():
    N = 0 #nr total de pasi
    S = 0 #suma de bani totala primita de A dela B 
    while True:
        N += 1
        moneda = random.choice(["stema", "ban"])
        if moneda == "ban":
            S -= 0.5
        else:
            z = random.choice([1, 2, 3, 4, 5, 6])
            S += z - 3
            break 
    return N, S

def histograma(p):

    N = 10000
    sume = []
    for _ in range(N):
        _, S = joc_masluit(p) if p is not None else joc()
        sume.append(S)

    print(f"Media lui S este {np.mean(sume)}")

    plt.hist(sume, bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.title(f'Distributia sumei de bani S primite de A de la B pt p = {p}' if p is not None else 'Distributia sumei de bani S primite de A de la B pt p = 1/2')
    plt.xlabel('S')
    plt.ylabel('Nr de jocuri')


def joc_masluit(p):
    N = 0
    S = 0
    while True:
        N += 1
        if random.random() < p: # stema cu probabilitatea p
            z = random.choice([1, 2, 3, 4, 5, 6])
            S += z - 3
            break
        else: # ban cu probabilitatea 1 - p
            S -= 0.5
    return N, S


def main():
    #b
    print(joc())

    #c
    histograma(p=None)
    plt.savefig("Lab01/tema1/histograme1.png", dpi=150)
    plt.close() 

    #d
    histograma(0.3)
    plt.savefig("Lab01/tema1/histograme2.png", dpi=150)
    plt.close() 

    histograma(0.7)
    plt.savefig("Lab01/tema1/histograme3.png", dpi=150)
    plt.close()

if __name__ == "__main__":
    main()
