#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Dobrodošli v igri Ugani število!")
print("Uganiti morate, katero število med 1 in 10 imam v mislih.")

while True:
    try:
        vneseno_stevilo = int(raw_input("Vnesi število: "))

    except ValueError:
        print("Ste res vnesli število med 1 in 10?")
        continue

    if vneseno_stevilo != 2:
        print("Žal niste uganili, poskusite ponovno.")
        continue

    else:
        print("Čestitamo, število je res 2!")
        break
