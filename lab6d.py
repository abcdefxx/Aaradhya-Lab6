#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: 2026/11/09
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

def times_ten(start_index: int, end_index: int):
    new_dictionary= {}
    for key in range(start_index, end_index+1):
        new_dictionary[key]= key*10
    return new_dictionary
def main():
    my_dictionary= times_ten(2,6)
    print(my_dictionary)

main() 
