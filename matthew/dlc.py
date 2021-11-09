from bs4 import BeautifulSoup
import requests

id_file = open('id_mappings.txt', 'r', encoding='utf-8')
languages_file = open('test_languages.txt', 'w', encoding='utf-8')

for line in id_file:
    if line == '':
        continue
    elif line == '+':
        continue

    game_name = line.split(',')[0]
    game_id = line.split(',')[1]
    languages_file.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    languages_file.write(game_name + ', ' + game_id)
    print(game_name + ', ' + game_id)

    URL = 'https://store.steampowered.com/app/' + game_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    language_table = soup.find(class_='game_language_options')

    #print(language_table)
    if language_table is None:
        continue

    languages = language_table.find_all(class_='ellipsis')

    for language in languages:
        if language == '':
            continue

        languages_file.write(language.text.strip() + '\n')

languages_file.close()
id_file.close()