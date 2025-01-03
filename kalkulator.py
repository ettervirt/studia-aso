#!/bin/env python3

# Autor Piotr Bołoz
# email: piboloz@student.wsb-nlu.edu.pl

print("Podaj liczby i w srodku znak operacji przykład 1 + 2")
liczba1 = float(input())
operacja = input()
liczba2 = float(input())

if operacja == "+":
    print(f"Dodawanie: {liczba1 + liczba2}")
elif operacja == "-":
    print(f"Odejmowanie: {liczba1 - liczba2}")
elif operacja == "*":
    print(f"Mnożenie: {liczba1 * liczba2}")
elif operacja == "/":
    if liczba2: 
        print(f"Dzielenie: {liczba1 / liczba2}")
    else:
        print("Nie dziel przez zero")
else:
    print("błedny wybór")
