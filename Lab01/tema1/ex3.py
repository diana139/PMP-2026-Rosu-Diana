# 3 frizeri
# 1ul (a)  - 3c/h
# al2 lea (b) - 6c/h
# al3 -lea (c) - 4c/h

# λ1 = 3 h^-1
# λ2 = 6 h^−1
# λ3 = 4 h^−1
# P('un client sa fie ales de  frizerul a/b/c') : P(a) = 3/13, P(b) = 6/13, P(c) = 4/13   
# (de ce?)       
# intr-o ora cei 3 frizeri servesc in total 3 + 6 + 4 = 13 clienti
# Un frizer mai rapid se elibereaza mai des, deci preia mai multi clienti:
# a preia 3 din 13, b preia 6 din 13, c preia 4 din 13                     
import numpy as np
import matplotlib.pyplot as plt
import arviz as az

lambdas = [3, 6, 4]
probabilities = [l / sum(lambdas) for l in lambdas]

def timp_servire():
    frizer = np.random.choice([0, 1, 2], p=probabilities)
    return np.random.exponential(1 / lambdas[frizer])

def main():
    n = 10000
    X = [timp_servire() for _ in range(n)]
    print(f"media lui X : {np.mean(X)}")
    print(f"deviatia standard : {np.std(X)}")
        
    az.plot_kde(np.array(X))
    plt.title("Densitatea aproximativa a lui X")
    plt.xlabel("X (ore)")
    plt.ylabel("Densitate")
    plt.savefig("Lab01/tema1/densitate_X.png", dpi=150)
    plt.close()

if __name__ == "__main__":
    main()