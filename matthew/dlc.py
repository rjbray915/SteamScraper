from bs4 import BeautifulSoup
import requests

id_file = open('SteamScraper/final/filtered_titles.txt', 'r', encoding='utf-8')
dlc_file = open('test_dlc.txt', 'w', encoding='utf-8')

for line in id_file:
    if line == '':
        continue
    elif line == '+':
        continue

    game_name = line.split(',')[0]
    game_id = line.split(',')[1]
    dlc_file.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    dlc_file.write(game_name + ', ' + game_id)

    game_id = str(281990)
    URL = 'https://store.steampowered.com/app/' + game_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    dlc_table = soup.find(class_='gameDlcBlocks')

    #print(language_table)
    if dlc_table is None:
        continue
    dlc_prices = dlc_table.find_all(class_ ='game_area_dlc_price')
    dlc_names = dlc_table.find_all(class_ ='game_area_dlc_name')
    print(dlc_prices)
   
    dlcs = [(name, price) for name in dlc_names for price in dlc_prices]
   
    print(dlc_names)
    for dlc in dlcs:
        if dlc == '':
            continue
        #dlc_file.write(dlc[0].strip() + ', ' +  dlc[1].strip() + '\n')
    break;
dlc_file.close()
id_file.close()