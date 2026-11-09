#!/usr/bin/env python3
# Author: Aaradhya Shreshta
# Date:11-09
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

def histogram(text):
    counts={}
    for letter in text:
        if letter == " ":
            continue 
        if letter in counts:
            counts[letter]= counts[letter] + 1
        else:
            counts[letter]= 1

    for letter, count in counts.items():
        print(letter, "*" * count)

def main():
    histogram("hello amma")
main()