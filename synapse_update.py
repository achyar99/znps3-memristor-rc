"""
Pulse-by-pulse conductance update of a memristor synapse, in the form given in the
Methods (eq. 1-2) of Ji et al., Nat. Commun. 16, 6899 (2025),
doi:10.1038/s41467-025-62306-8:

    potentiation:  G[n+1] = G[n] + a_p * exp(-b_p * (G[n] - Gmin) / (Gmax - Gmin))
    depression:    G[n+1] = G[n] - a_d * exp(-b_d * (Gmax - G[n]) / (Gmax - Gmin))

The parameters below are illustrative, chosen only to show the shape of the curve.
"""

import matplotlib.pyplot as plt
import numpy as np

GMIN, GMAX = 1.0, 10.0
A_P, B_P = 0.25, 3.0
A_D, B_D = 0.25, 3.0


def potentiate(G):
    return min(G + A_P * np.exp(-B_P * (G - GMIN) / (GMAX - GMIN)), GMAX)


def depress(G):
    return max(G - A_D * np.exp(-B_D * (GMAX - G) / (GMAX - GMIN)), GMIN)


if __name__ == "__main__":
    G, trace = GMIN, []
    for _ in range(100):
        G = potentiate(G); trace.append(G)
    for _ in range(100):
        G = depress(G); trace.append(G)
    plt.plot(trace, ".", ms=3)
    plt.xlabel("Pulse number")
    plt.ylabel("Conductance (a.u.)")
    plt.title("Nonlinear potentiation and depression")
    plt.show()
