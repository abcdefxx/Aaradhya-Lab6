#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: 2026-11-09
# Purpose: Traverse dictionary.
# Usage: ./lab6e.py

my_dict = {"switzerland" : "Alps", "United States" : "Alska Range", "Armenia" : "Caucasus", "Argentina" : "Andes", "Karakoram" : "Pakistan"}


for key, value in my_dict.items():
    print(f"{key} : {value}")