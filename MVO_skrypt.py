import numpy as np
import pandas as pd
from mealpy import FloatVar, MVO
import time


# FUNKCJA CELU (Hypersphere)
def hypersphere(solution):
    return np.sum(solution ** 2)


# DEFINICJA PROBLEMU
problem_dict = {
    "bounds": FloatVar(lb=[-5.0] * 10, ub=[5.0] * 10),
    "obj_func": hypersphere,
    "minmax": "min",
    "log_to": None  # bez spamu w konsoli
}

# KONFIGURACJE PARAMETRÓW (GridSearch 3x3x2)
# Intensywność pojawiania sie tuneli czasoprzestrzennych
warianty_wep = [
    {"typ": "Mało tuneli", "wep_min": 0.1, "wep_max": 0.5},
    {"typ": "Standard", "wep_min": 0.2, "wep_max": 1.0},
    {"typ": "Dużo tuneli", "wep_min": 0.49, "wep_max": 2.5}
]
# Rozmiar populacji - liczba wszechświatów
populacje = [30, 60, 100]

# Czas ewolucji - liczba epok
epoki = [50, 150]

historia_wynikow = []

print("Start symulacji Multi-Verse Optimizer dla funkcji Hypersphere...")

# GŁÓWNA PĘTLA OBLICZENIOWA
licznik = 1
for epoka_val in epoki:
    for pop in populacje:
        for wep in warianty_wep:
            nazwa_konf = f"Epoki: {epoka_val} | Pop: {pop} | Tunele: {wep['typ']}"
            print(f"[{licznik}/18] Badam: {nazwa_konf}")

            model = MVO.OriginalMVO(epoch=epoka_val, pop_size=pop, wep_min=wep['wep_min'], wep_max=wep['wep_max'])

            start_time = time.time()
            model.solve(problem_dict, seed=1)
            end_time = time.time()
            czas_wykonania = end_time - start_time
            najlepsze_wyniki = model.history.list_global_best_fit

            for aktualna_epoka, wynik in enumerate(najlepsze_wyniki):
                historia_wynikow.append({
                    "Liczba_Epok_Max": epoka_val,
                    "Rozmiar_Populacji": pop,
                    "Typ_Tuneli": wep['typ'],
                    "Konfiguracja": nazwa_konf,
                    "Generacja": aktualna_epoka + 1,
                    "Najlepszy_wynik": wynik,
                    "Czas_s": czas_wykonania
                })
            licznik += 1

# ZAPIS DO PLIKU CSV
df = pd.DataFrame(historia_wynikow)
df.to_csv("wyniki_mvo.csv", index=False)
print("\nKoniec! Wyniki zapiasne do 'wyniki_mvo.csv'.")
