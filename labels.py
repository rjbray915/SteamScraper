from bs4 import BeautifulSoup
import requests

id_file = open('id_mappings.txt', 'r', encoding='utf-8')
tags_file = open('test_labels.txt', 'w', encoding='utf-8')

for line in id_file:
    if line == '':
        continue
    elif line == '+':
        continue

    game_name = line.split(',')[0]
    game_id = line.split(',')[1]
    tags_file.write(game_name + ', ' + game_id)
    print(game_name + ', ' + game_id)
    

    URL = 'https://store.steampowered.com/app/' + game_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.find_all(class_='app_tag')

    for tag in tags:
        if tag == '':
            continue

        tags_file.write(tag.text.strip() + ', ')


tags_file.close()
id_file.close()