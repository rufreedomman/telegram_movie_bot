#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import dotenv
import imdb
import requests

dotenv.load_dotenv()

instance = imdb.IMDb()


def get_movie_info(movieTitle):
    url = "https://www.omdbapi.com"
    omdb_api_key = os.getenv("OMDB_API_KEY")
    data = {"apiKey": omdb_api_key, "t": movieTitle}
    response = requests.get(url, data).json()

    if response.get("Response") != "True":
        return None

    movie_info = dict()
    movie_info["title"] = response.get("Title")
    movie_info["year"] = response.get("Year")
    movie_info["plot"] = response.get("Plot")
    movie_info["actors"] = response.get("Actors")
    movie_info["ratings"] = response.get("Ratings")
    movie_info["imdb_rating"] = response.get("imdbRating")

    return movie_info
