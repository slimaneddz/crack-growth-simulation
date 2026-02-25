import matplotlib.pyplot as plt
from typing import List

def plot_a_vs_N(N: List[int], a: List[float]) -> None:
    plt.figure()
    plt.plot(N, a)
    plt.xlabel("Cycles N")
    plt.ylabel("Crack length a (m)")
    plt.title("Crack growth: a vs N")
    plt.grid(True)
    plt.savefig("a_vs_N.png", dpi=200, bbox_inches="tight")
    plt.show(block=True)

def plot_dK_vs_a(a: List[float], dK: List[float]) -> None:
    plt.figure()
    plt.plot(a, dK)
    plt.xlabel("Crack length a (m)")
    plt.ylabel("ΔK (units depend on Δσ)")
    plt.title("Stress intensity range: ΔK vs a")
    plt.grid(True)
    plt.savefig("dK_vs_a.png", dpi=200, bbox_inches="tight")
    plt.show(block=True)