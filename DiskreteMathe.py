import hashlib
import itertools
import string

letters = list(string.ascii_letters)
digits = list(string.digits)
allChars = letters + digits

def brute_force_system1():
    for o in itertools.product(allChars, repeat=5):
        input = "".join(o)
        print(input + "   " + hash)
        hash = hashlib.sha1(input.encode('utf-8')).hexdigest()
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


def brute_force_system4():
    for len in range(1, 4):
        for o in itertools.product(allChars, repeat=len):
            input = "".join(o)
            hash = hashlib.sha1(input.encode('utf-8')).hexdigest()
            print(input + "   " + hash + "     ")
            if hash == "7e240de74fb1ed08fa08d38063f6a6a91462a815":
                print("INPUT: ", input)
                return input

#Ergebnis System1 INPUT = X42a0
#brute_force_system1()

#Ergebnisse für System 2 & 3 konnten nicht berechnet werden,
#weil die Zeit zu lange dauert. 
brute_force_system2()
#brute_force_system3()
#brute_force_system4()
