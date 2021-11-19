from bs4 import BeautifulSoup
import requests
import multiprocessing as mp



def dlc(game_name, game_id):
    dlc_file = open('test_dlc.txt', 'a', encoding='utf-8')
    i = 0

    
 
    URL = 'https://store.steampowered.com/app/' + game_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    dlc_table = soup.find(class_='gameDlcBlocks')

    # print(language_table)
    if dlc_table is None:
        #dlc_file.write('\n')
        return

    dlc_prices = dlc_table.find_all(class_='game_area_dlc_price')
    dlc_names = dlc_table.find_all(class_='game_area_dlc_name')
    dlcs = [(name.text.strip(), price.text.strip())
               for name, price in zip(dlc_names, dlc_prices)]
    if len(dlcs) != 0:
        dlc_file.write(game_name + ', ' + game_id)
    for dlc in dlcs: 
        if dlc == '':
            continue
        dlc_file.write(', ' + dlc[0] + ', ' + dlc[1])
    dlc_file.write('\n')
    dlc_file.close()

def main():
    id_file = open('SteamScraper/final/filtered_titles.txt', 'r', encoding='utf-8')

    arguments = []
    for line in id_file:
        if line == '':
            continue
        elif line == '+':
            continue

        game_name = line.split(',')[0].strip()
        game_id = line.split(',')[1].strip()
        arguments.append((game_name, game_id))
    
    with mp.Pool(10) as p:
        p.starmap(dlc, arguments)
#dlc(game_name, game_id)
    id_file.close()

if __name__ == "__main__":
    main()
