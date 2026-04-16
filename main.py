#!/usr/bin/env python3
"""
Mastermind Game
Author: brainiacweb-tech
"""
import random

COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']
CODE_LEN = 4
MAX_TRIES = 10

def make_code(): return [random.choice(COLORS) for _ in range(CODE_LEN)]

def score(secret, guess):
    exact = sum(s == g for s, g in zip(secret, guess))
    color = sum(min(secret.count(c), guess.count(c)) for c in set(COLORS)) - exact
    return exact, color

def play():
    secret = make_code()
    print("\n" + "=" * 42)
    print("           MASTERMIND")
    print("=" * 42)
    print(f"Colors: {' '.join(COLORS)}")
    print(f"Crack the {CODE_LEN}-color code in {MAX_TRIES} tries.")
    print("  Black peg = right color, right position")
    print("  White peg = right color, wrong position\n")
    for attempt in range(1, MAX_TRIES + 1):
        raw = input(f"Try {attempt}: ").strip().upper().split()
        if len(raw) != CODE_LEN or not all(c in COLORS for c in raw):
            print(f"Enter {CODE_LEN} colors from {COLORS}"); continue
        b, w = score(secret, raw)
        print(f"  Black: {b}  White: {w}")
        if b == CODE_LEN:
            print(f"\nYou cracked the code: {secret}!"); return
    print(f"\nOut of tries! Code was: {secret}")

if __name__ == "__main__":
    while True:
        play()
        if input("\nPlay again? (y/n): ").strip().lower() != 'y':
            break
