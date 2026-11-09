#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: 11-09
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

def add_movie(database, name, director, year, runtime):
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)

def main():
    database=[]
    add_movie(database, "The Dark Knight", "Christopher Nolan", 2008, 152)
    add_movie(database, "The Dark Knight Rises", "Christopher Nolan", 2012, 164)
    add_movie(database, "Inception", "Christopher Nolan", 2010, 148)
    add_movie(database, "Interstellar", "Christopher Nolan", 2014, 169)

    for movie in database:
     print(movie)
 
main()