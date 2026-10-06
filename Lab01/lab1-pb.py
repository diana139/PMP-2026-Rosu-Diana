import random
from fractions import Fraction

#a)
def experiment():
    urna = ["rosu"] * 3 + ["albastru"] * 4 + ["negru"] * 2

    zar = random.randint(1, 6)
    if zar in (2, 3, 5):       
        urna.append("negru")
    elif zar == 6:
        urna.append("rosu")
    else: 
        urna.append("albastru")

    return random.choice(urna)

print(experiment())


#b)
N = 100000
rosii = sum(1 for _ in range(N) if experiment() == "rosu")
p_estimat = rosii / N
print(f"Probabilitate estimata: {p_estimat:.4f}")



#c)
p_teoretic = Fraction(1, 2) * Fraction(3, 10) + Fraction(1, 6) * Fraction(4, 10) + Fraction(1, 3) * Fraction(3, 10)

print(f"Probabilitate teoretica: {p_teoretic} ≈ {float(p_teoretic):.4f}")
print(f"Probabilitate estimata: {p_estimat:.4f}")
print(f"Diferenta absoluta: {abs(p_estimat - float(p_teoretic)):.4f}")
