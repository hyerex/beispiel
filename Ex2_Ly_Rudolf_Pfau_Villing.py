# Andreas Ly
# Robin Rudolf
# Timmy Pfau
# Sascha Villing

import hashlib
import itertools
import string

letters = list(string.ascii_letters)
digits = list(string.digits)
allChars = letters + digits

def brute_force_system1():
    for o in itertools.product(allChars, repeat=5):
        input = "".join(o)
        hash = hashlib.sha1(input.encode('utf-8')).hexdigest()
        print(input + "   " + hash)
        if hash == "5aea476328379d3bff2204501bb57aa8b4268fac":
            print("INPUT: ", input)
            return input


def brute_force_system2():
    for o in itertools.product(allChars, repeat=10):
        input = "".join(o)
        hash = hashlib.sha1(input.encode('utf-8')).hexdigest()
        print(input + "   " + hash)
        if hash == "d31d62ed0af022248e28fc0dc4a9580217987e55":
            print("INPUT: ", input)
            return input

def brute_force_system3():
    for len in range(5, 11):
        for o in itertools.product(allChars, repeat=len):
            input = "".join(o)
            hash = hashlib.sha1(input.encode('utf-8')).hexdigest()
            print(input + "   " + hash)
            if hash == "66ceeafde8453dda201978b2b497b9c85d4b6da5":
                print("INPUT: ", input)
                return input

brute_force_system1()
brute_force_system2()
brute_force_system3()

# Ergebnis System1 INPUT = X42a0
# Ergebnisse für System 2 & 3 konnten nicht berechnet werden,
# weil der Input viel zu lang ist und deswegen zu viel Zeit braucht.
# Bei dem schnellsten Computer von uns hat die Berechnung für System 1 bereits 3 Stunden gedauert und das bei 62^5 Möglichkeiten (916.132.832)
#
# System2 hat 62^10 Möglichkeiten (839.299.365.868.340.224). 
# System2 durchlief bereits 14 Stunden und man ist erst bei aaaacHt2ga gelandet.
#
# System3 hat 62^5 + 62^6 + 62^7 + 62^8 + 62^9 + 62^10 verschiedene Möglichkeiten (853.058.371.851.163.296).
# System3 durchlief auf einem anderen PC 20 Stunden und man ist bei aaaapF2EAn gelandet.
# Dies mit einem normalen Computer zu berechnen würde praktisch Jahre dauern.