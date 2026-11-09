#!/usr/bin/env python3
# Author: Aaradhya Shrestha 
# Date: 11-09
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

def buildtheSet(divisor):
    new_set= set()
    for number in range(0,101):
        if number % divisor == 0:
            new_set.add(number)
    return new_set

def s3_and_s5_not_s7(s3, s5, s7):
    in_both= s3.intersection(s5)
    result= in_both.difference(s7)
    return result

def main():
    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7= buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    final_set= s3_and_s5_not_s7(s3, s5, s7)
    print("s3 and s5 not s7: ", final_set)

main()
