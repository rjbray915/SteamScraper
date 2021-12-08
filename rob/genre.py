from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool

id_file = open('id_mappings.txt', 'r', encoding='utf-8')
genre_file = open('test_labels.txt', 'w', encoding='utf-8')

def process_soup(id):
    URL = 'https://store.steampowered.com/app/' + game_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    genre = soup.find('div', {'id' : 'genresAndManufacturer'})\
        .findNext('a').text.strip()

    genre_file.write(genre + ', ')

id_list = list()
for line in id_file:
    if line == '':
        continue
    elif line == '+':
        continue

    game_name = line.split(',')[0]
    game_id = line.split(',')[1]
    genre_file.write(game_name + ', ' + game_id)
    print(game_name + ', ' + game_id)
    id_list.append(game_id)

with Pool(processes=4) as p:
    p.map(process_soup, id_list)


genre_file.close()
id_file.close()
