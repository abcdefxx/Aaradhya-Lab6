#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: 2026-11-09
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py

def buildtheSet(divisor):
    new_set= set()
    for number in range(0,101):
        if number % divisor == 0:
            new_set.add(number)
    return new_set

def s3_or_s5(s3,s5):
    s3ors5= s3.union(s5).difference(s3.intersection(s5))
    return s3ors5

def main():
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s3ors5= s3_or_s5(s3, s5)
    print("s3ors5: ", s3ors5)

    
main()