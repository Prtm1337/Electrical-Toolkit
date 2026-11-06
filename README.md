# Electrical Toolkit

A small command-line calculator for common Electrical Engineering formulas, written in Python.
Built as a first-year learning project at VSSUT, Burla.

## Features
- Ohm's law (give any two of V, I, R)
- Series and parallel resistance
- Power (P = V x I)
- Voltage divider
- RC time constant and capacitor charging voltage
- Ideal transformer secondary voltage and turns ratio

## How to run
Requires Python 3.8+ (no extra libraries needed).

```bash
python electrical_toolkit.py
```

## Example
```
Choose: 3
  Resistors (space-separated, ohms): 100 220 330
  Total: 56.9 ohm
```

## Use as a module
```python
from electrical_toolkit import parallel_resistance, rc_time_constant

print(parallel_resistance(100, 220, 330))
print(rc_time_constant(10_000, 100e-6))  # 1.0 second
```

## Ideas for next steps
- Add a plot of the RC charging curve with matplotlib
- Add three-phase power calculations
- Add unit tests

## Author
Pritam Panda - B.Tech Electrical Engineering, VSSUT Burla
