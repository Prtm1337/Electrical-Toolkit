"""Electrical Toolkit - a small command-line calculator for common EE formulas.

Run:  python electrical_toolkit.py
Only the Python standard library is used.
"""

import math


def ohms_law(v=None, i=None, r=None):
    """Give any two of V, I, R (volts, amps, ohms) and get the missing one."""
    given = [x is not None for x in (v, i, r)]
    if sum(given) != 2:
        raise ValueError("Provide exactly two of v, i, r.")
    if v is None:
        return {"v": i * r}
    if i is None:
        return {"i": v / r}
    return {"r": v / i}


def series_resistance(*resistors):
    """Total resistance of resistors in series."""
    return sum(resistors)


def parallel_resistance(*resistors):
    """Total resistance of resistors in parallel."""
    if any(r == 0 for r in resistors):
        return 0.0
    return 1 / sum(1 / r for r in resistors)


def power(v, i):
    """Electrical power in watts: P = V * I."""
    return v * i


def voltage_divider(vin, r1, r2):
    """Output voltage across r2 in a two-resistor divider."""
    return vin * r2 / (r1 + r2)


def rc_time_constant(r, c):
    """Time constant tau = R * C (seconds)."""
    return r * c


def rc_charge_voltage(vs, r, c, t):
    """Capacitor voltage t seconds after charging starts from 0 V."""
    return vs * (1 - math.exp(-t / (r * c)))


def transformer_secondary(v_primary, n_primary, n_secondary):
    """Ideal transformer: secondary voltage and turns ratio."""
    ratio = n_primary / n_secondary
    return {"v_secondary": v_primary / ratio, "turns_ratio": ratio}


def _ask(label):
    return float(input(f"  {label}: "))


def _ask_optional(label):
    raw = input(f"  {label} (leave blank if unknown): ").strip()
    return float(raw) if raw else None


def _list(label):
    raw = input(f"  {label} (space-separated, ohms): ")
    return [float(x) for x in raw.split()]


MENU = """
=== Electrical Toolkit ===
1. Ohm's law
2. Series resistance
3. Parallel resistance
4. Power (P = V x I)
5. Voltage divider
6. RC time constant and charging
7. Ideal transformer
0. Exit
"""


def main():
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        try:
            if choice == "0":
                print("Bye!")
                break
            elif choice == "1":
                print("  Result:", ohms_law(_ask_optional("V"), _ask_optional("I"), _ask_optional("R")))
            elif choice == "2":
                print(f"  Total: {series_resistance(*_list('Resistors')):.4g} ohm")
            elif choice == "3":
                print(f"  Total: {parallel_resistance(*_list('Resistors')):.4g} ohm")
            elif choice == "4":
                print(f"  Power: {power(_ask('V (volts)'), _ask('I (amps)')):.4g} W")
            elif choice == "5":
                print(f"  Vout: {voltage_divider(_ask('Vin'), _ask('R1'), _ask('R2')):.4g} V")
            elif choice == "6":
                r, c = _ask("R (ohms)"), _ask("C (farads)")
                vs, t = _ask("Supply voltage (V)"), _ask("Time t (s)")
                print(f"  Tau: {rc_time_constant(r, c):.4g} s")
                print(f"  Capacitor voltage at t: {rc_charge_voltage(vs, r, c, t):.4g} V")
            elif choice == "7":
                res = transformer_secondary(_ask("Primary V"), _ask("Primary turns"), _ask("Secondary turns"))
                print(f"  Secondary V: {res['v_secondary']:.4g} V  (turns ratio {res['turns_ratio']:.4g}:1)")
            else:
                print("  Invalid choice, try again.")
        except (ValueError, ZeroDivisionError) as err:
            print(f"  Error: {err}")


if __name__ == "__main__":
    main()
