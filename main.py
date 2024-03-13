from nfo import parse_nfo
from audio import audio_stream_names_safe
from utils import *
import os
import json

movies = []

movie_dir = "/path/to/dir"

if __name__ == "__main__":
    for movie in os.listdir(movie_dir):
        movie_path = os.path.join(movie_dir, movie)
        if os.path.isdir(movie_path):
            found = False
            current_info = {}
            for file in os.listdir(movie_path):
                if is_nfo(file):
                    nfo = parse_nfo(os.path.join(movie_path, file))
                    current_info.update(nfo)
                if is_movie(file):
                    audio_streams = audio_stream_names_safe(os.path.join(movie_path, file))
                    current_info.update({"audio_streams" : audio_streams})
                
            if "title" in current_info:
                movies.append(current_info)

with open("movies.json", "w") as out:
    json.dump(movies, out)
