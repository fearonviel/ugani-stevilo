#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Dobrodošli v igri Ugani število!")
print("Uganiti morate, katero število med 1 in 10 imam v mislih.")

moje_stevilo = 2

while True:
    try:
        vneseno_stevilo = int(raw_input("Vnesi število: "))

    except ValueError:
        print("Ste res vnesli število med 1 in 10?")
        continue

    if vneseno_stevilo < moje_stevilo:
        print("Število je višje od " + str (vneseno_stevilo) + ".")

    elif vneseno_stevilo > moje_stevilo:
        print("Število je nižje od " + str (vneseno_stevilo) + ".")

    elif vneseno_stevilo == moje_stevilo:
        print("Čestitamo, število je res 2!")
        break
