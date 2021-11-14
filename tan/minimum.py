from bs4 import BeautifulSoup
import requests

id_file = open('tan_filtered.txt', 'r', encoding='utf-8')
minimums_file = open('test_minimum.txt', 'w', encoding='utf-8')

for line in id_file:
    if line == '':
        continue
    elif line == '+':
        continue

    game_name = line.split(',')[0]
    game_id = line.split(',')[1]
    minimums_file.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    minimums_file.write(game_name + ', ' + game_id)
    print(game_name + ', ' + game_id)

    #https://store.steampowered.com/app/1690670
    URL = 'https://store.steampowered.com/app/' + game_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    minimum_table = soup.find(class_='game_area_sys_req_leftCol')

    if minimum_table is None:
        continue

    #minimums = minimum_table.find_all(class_='bb_ul')
    minimums = minimum_table.find_all('li')

    for minimum in minimums:
        if minimum == '':
            continue

        minimums_file.write(minimum.text.strip()+'\n')
        print(minimum.text.strip('')+'\n')

minimums_file.close()

id_file.close()
