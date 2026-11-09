#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date:2026-11-09
# Purpose: Create Sets.
# Usage: ./lab6a.py

def buildtheSet(divisor):
    new_set= set()
    for number in range(0,101):
        if number % divisor == 0:
            new_set.add(number)
    return new_set
    
def main():
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s11 = buildtheSet(11)
    print("s11: ", s11)

main()
