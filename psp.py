#!/usr/bin/env python3

import sys
import math

from primesieve import primes as psPrimes

def getPrimes(ceiling):
    primes = [1,2]
    for i in range(2,ceiling+1):
        if i not in primes[1:]:
            factorCheck = False
            for p in primes[1:]:
                if i % p == 0:
                    factorCheck = True
            if not factorCheck:
                primes.append(i)
    return primes

def getPmults(primes):
    pmults = []
    pm = 1
    for p in primes:
        pm = pm * p
        pmults.append(pm)
    return pmults

def isDivisible(number, factor):
    if number % factor == 0:
        return True
    else:
        return False

def convertToPsp(number,primes,pmults):
    if number == 0:
        return ' '
    elif number == 1:
        return '0'
    else:
        result = ''
        i = 1
        for p in reversed(primes):
            if p == 1:
                pass
            else:
                if not isDivisible(number, p):
                    result = result + '0'
                else:
                    result = result + '1'

            i += 1
        return result




def main(values):
    iterations = int(values[0])

    results = []
    for i in range(iterations+1):
        #primes = getPrimes(i)
        primes = psPrimes(i+1)
        #print(f"valid primes for {i}: {len(primes)} {primes}")

        pmults = getPmults(primes)
        #print(f"respective multiplicants: {len(pmults)} {pmults}")
        results.append(convertToPsp(i,primes,pmults))


    pspStrLen = 0
    totalLen = len(results[len(results)-1])
    for r in range(len(results)):
        pR = totalLen - len(results[r])
        padding = ''.join([' ' for p in range(pR)])
        try:
            if len(results[r+1]) > pspStrLen:
                end = "\n"
                pspStrLen = len(results[r+1])
            else:
                end = '\t'
        except:
            end = ""

        try:
            binaryRep = int(results[r],2)
        except:
            binaryRep = '?'
        result = results[r]
        results[r] = f"{padding}{result}"
        print(f"{results[r]}", end=end)



if __name__ == "__main__":
    if sys.argv[1:] != []:
        main(values=sys.argv[1:])
    else:
        print("no arguments provided, requires the following: iterations (integer, how many numbers to try);")
