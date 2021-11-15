from bs4 import BeautifulSoup
import requests

id_file = open('tan_filtered.txt', 'r', encoding='utf-8')
recommended_file = open('test_recommended.txt', 'w', encoding='utf-8')

for line in id_file:
    if line == '':
        continue
    elif line == '+':
        continue

    game_name = line.split(',')[0]
    game_id = line.split(',')[1]
    recommended_file.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    recommended_file.write(game_name + ', ' + game_id)
    print(game_name + ', ' + game_id)

    #https://store.steampowered.com/app/1690670
    URL = 'https://store.steampowered.com/app/' + game_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    recommended_table = soup.find(class_='game_area_sys_req_rightCol')

    if recommended_table is None:
        continue

    #recommendeds = recommended_table.find_all(class_='bb_ul')
    recommendeds = recommended_table.find_all('li')

    for recommended in recommendeds:
        if recommended == '':
            continue

        recommended_file.write(recommended.text.strip()+'\n')
        print(recommended.text.strip()+'\n')

recommended_file.close()
id_file.close()
