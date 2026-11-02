#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""A minimal dice roller with configurable dice and a Tkinter interface."""
from __future__ import annotations

import argparse
import secrets
import tkinter as tk


def roll(sides: int = 6, count: int = 1) -> tuple[int, ...]:
    if not 2 <= sides <= 1000:
        raise ValueError("sides must be between 2 and 1000")
    if not 1 <= count <= 20:
        raise ValueError("count must be between 1 and 20")
    return tuple(secrets.randbelow(sides) + 1 for _ in range(count))


class DiceApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Dice Simulator · Hamdy Abou El Anein")
        self.geometry("480x390")
        self.minsize(400, 340)
        self.configure(bg="#101827")
        self.sides = tk.IntVar(value=6)
        self.count = tk.IntVar(value=1)
        self.result = tk.StringVar(value="Ready to roll")
        self.detail = tk.StringVar(value="Choose your dice and roll.")
        box = tk.Frame(self, bg="#101827", padx=25, pady=25)
        box.pack(fill="both", expand=True)
        tk.Label(box, text="DICE SIMULATOR", font=("DejaVu Sans", 13, "bold"),
                 bg="#101827", fg="#8bd6c1").pack(pady=(0, 20))
        controls = tk.Frame(box, bg="#101827")
        controls.pack()
        for label, variable, options in (
            ("Sides", self.sides, (4, 6, 8, 10, 12, 20, 100)),
            ("Dice", self.count, (1, 2, 3, 4, 5, 6)),
        ):
            group = tk.Frame(controls, bg="#101827")
            group.pack(side="left", padx=14)
            tk.Label(group, text=label, bg="#101827", fg="#dbe5f0").pack()
            tk.OptionMenu(group, variable, *options).pack()
        tk.Label(box, textvariable=self.result, font=("DejaVu Sans", 38, "bold"),
                 bg="#101827", fg="#f2c879").pack(pady=(30, 8))
        tk.Label(box, textvariable=self.detail, font=("DejaVu Sans", 10),
                 bg="#101827", fg="#b8c7d8", wraplength=400).pack()
        tk.Button(box, text="Roll dice", command=self.throw, font=("DejaVu Sans", 11, "bold"),
                  bg="#7ddcc0", fg="#10211c", relief="flat", padx=24, pady=10).pack(pady=22)
        self.bind("<space>", lambda _event: self.throw())

    def throw(self) -> None:
        values = roll(self.sides.get(), self.count.get())
        self.result.set(str(sum(values)))
        self.detail.set(" + ".join(map(str, values)) + f"  ·  {len(values)}d{self.sides.get()}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--roll", action="store_true", help="Roll in the terminal")
    parser.add_argument("--sides", type=int, default=6)
    parser.add_argument("--count", type=int, default=1)
    args = parser.parse_args()
    if args.roll:
        print(" ".join(map(str, roll(args.sides, args.count))))
    else:
        DiceApp().mainloop()


if __name__ == "__main__":
    main()
