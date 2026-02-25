from dataclasses import dataclass
from typing import List, Tuple
from .models import delta_K, paris_da_dN

@dataclass
class Params:
    delta_sigma: float
    Y: float
    C: float
    m: float
    a0: float
    a_crit: float
    K_IC: float
    dN: int
    DK_th: float
    max_N: int
def simulate(params: Params) -> Tuple[List[int], List[float], List[float]]:
    N = 0
    a = params.a0

    N_list = [N]
    a_list = [a]
    dK_list = [delta_K(params.delta_sigma, params.Y, a)]

    while True:
        # Safety stop: max cycles
        if N >= params.max_N:
            break

        dK = delta_K(params.delta_sigma, params.Y, a)

        # Stop conditions
        if a >= params.a_crit or dK >= params.K_IC:
            break

        # Below threshold: no crack growth; just accumulate cycles
        if dK < params.DK_th:
            N += params.dN
            N_list.append(N)
            a_list.append(a)
            dK_list.append(dK)
            continue

        # Paris law growth (above threshold)
        da_dN = paris_da_dN(params.C, params.m, dK)
        da = da_dN * params.dN

        # Safety: if something weird happens
        if da <= 0:
            break

        a += da
        N += params.dN

        N_list.append(N)
        a_list.append(a)
        dK_list.append(delta_K(params.delta_sigma, params.Y, a))

        if len(N_list) > 2_000_000:
            raise RuntimeError("Too many steps; check parameters.")

    return N_list, a_list, dK_list