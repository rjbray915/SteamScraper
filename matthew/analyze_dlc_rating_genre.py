import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

import analyze_rating
import analyze_dlc

def clean_file():
    with open("matthew/scrapeResults.csv", encoding="utf-8") as dlc:
        rows = []
        for line in dlc.readlines():
            rows.append(line.split(','))
    with open("matthew/genre.csv", "w", encoding="utf-8") as w:
        record = set()
        for row in rows:
            if row[1] not in record:
                if row[-2] != '':
                    w.write(row[1] + ", " + row[-2] + "\n")
                record.add(row[1])

def dlc_by_genre(genres, dlc_list, genre):
    values = [dlc for dlc in dlc_list if dlc[1].strip() in genres[genre]]
    print(genre.upper())
    analyze_dlc.analyze(values, genre)
            

#rating_list = analyze_rating.read_rating()
dlc_list = analyze_dlc.read_dlc()

with open("matthew/genre.csv", encoding="utf-8") as dlc:
    rows = []
    for line in dlc.readlines():
        rows.append(line.strip().split(','))

genres = {}
for row in rows:
    genre = row[1].strip()
    if genre not in genres:
            genres[genre] = [row[0]]
    else:
        if row[0] not in genres[genre]:
            genres[genre].append(row[0])

dlc_by_genre(genres, dlc_list, 'Action')
dlc_by_genre(genres, dlc_list, 'Adventure')
dlc_by_genre(genres, dlc_list, 'Casual')
dlc_by_genre(genres, dlc_list, 'Indie')
dlc_by_genre(genres, dlc_list, 'Simulation')