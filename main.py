import random
import csv
import re

#A class to store username
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#A function to handle other functions in the code
def main():
    print("*" * 55)
    print("Welcome to the Movie Recommender System!")
    print("*" * 55)
    print(user_info(input("What is your name? ").strip(), input("How old are you? ") ))
    funny, genre, year = values(input("On a scale of one to ten, how funny should the movie be? "),
                          input("What genre \n A. Romance \n B. Comedy \n C. Romantic Comedy \n D. Action \n Genre: ").upper(),
                          input("What should be the minimum year? "))
    print(recommender(funny, genre, User.age, year))

#A function to request and store username
def user_info(name, age):
    if name == "" or name in (" ", ".", ",", "!") or len(name) <= 1 or not age.isdigit():
        raise ValueError("Invalid name")
    else:
        User.name = name
        User.age  = int(age)
        return(f"Hello {User.name}!")

#Request user input for recommender values
def values(funny, genre, year):
    if not funny.isdigit():
        raise ValueError("Response should a number")

    elif int(funny) not in (1,2,3,4,5,6,7,8,9,10):
        raise ValueError("Response should be from 1 to 10")

    if genre not in ("A", "B", "C", "D"):
        raise ValueError("Choose from A - D")

    if not re.search(r"\d{4}", year):
        raise ValueError("Invalid year")
    return (int(funny), genre, int(year))

def recommender(funny, genre, age, year):
    genres = {"A": "romance", "B": "comedy", "C": "romantic comedy", "D":"action" }
    genre = genres[genre]
    movies = []
    with open("movies.csv", "r" ) as file:
        file = csv.DictReader(file)
        for row in file:
            if int(row["age"]) <= age and int(row["funny"]) == funny and row["genre"] == genre and int(row["year"]) >= year:
                movies.append(row["movies"])
        if len(movies) == 0:
            return "Movie does not exist"
        else:
            return f"Movie Recommendation: {random.choice(movies)}"

if __name__ == "__main__":
    main()