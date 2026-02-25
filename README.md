# Fatigue Crack Propagation Simulator

## Overview

This project implements a fatigue crack growth simulator based on Linear Elastic Fracture Mechanics (LEFM).

The crack propagation is modeled using:

- Stress Intensity Factor (ΔK)
- Paris' Law
- Numerical time integration

The objective is to simulate crack growth under cyclic loading and evaluate structural integrity and fatigue life.

---

## Governing Equations

Stress Intensity Factor:

ΔK = Y * Δσ * sqrt(πa)

Paris Law:

da/dN = C (ΔK)^m

Where:
- a = crack length
- Δσ = stress range
- Y = geometry correction factor
- C, m = material constants

---

## Features

- Numerical integration of crack growth
- Fatigue life prediction
- Visualization of:
  - Crack length vs number of cycles
  - Stress intensity factor vs crack length
- Configurable parameters via JSON file

---

## Example Output

The simulation stops when:
- Crack length reaches critical value
OR
- Stress intensity factor exceeds fracture toughness (K_IC)

---

## Applications

- Pipeline integrity assessment
- Structural components under cyclic loading
- Failure risk estimation
- Engineering education and research

---

## Requirements

