import json
import csv
from pathlib import Path
from .solver import Params, simulate
from .plotting import plot_a_vs_N, plot_dK_vs_a

def load_params(config_path: str) -> Params:
    data = json.loads(Path(config_path).read_text(encoding="utf-8"))
    return Params(**data)

def run():
    print("Running crack growth simulation...")
    params = load_params("config.json")
    N, a, dK = simulate(params)
    with open("results.csv", "w", newline="") as f:
         w = csv.writer(f)
    w.writerow(["N", "a_m", "DeltaK"])
    for i in range(len(N)):
        w.writerow([N[i], a[i], dK[i]])
    print("Saved results.csv")
    print(f"Stopped at N={N[-1]} cycles, a={a[-1]:.6f} m, ΔK={dK[-1]:.3f}")
    plot_a_vs_N(N, a)
    plot_dK_vs_a(a, dK)

if __name__ == "__main__":
    run()