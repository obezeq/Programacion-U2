#!/usr/bin/env python3

import os

num = input("Introduce un número entero: ")

try:
    if str(float(num)) == f"{num}.0":
        num = int(num)
        list = []

        n = num
        while n >= 0:
            print(n)
            n = n - 2
            n.

    else:
        print("ERROR: No has introducido un número entero.")
        os._exit(0)
except ValueError:
    print("ERROR: No has introducido un número!")