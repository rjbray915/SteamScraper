from multiprocessing.spawn import freeze_support
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool

def scrape_page(p_name, p_id):
    write_file = open('test_genre_descr.txt', 'a', encoding='utf-8')
    #print(p_name + ', ' + p_id)

    URL = 'https://store.steampowered.com/app/' + p_id
    try:
        page = requests.get(URL)
    except:
        print(f'REQUEST ERROR. Continuing...')
        return

    soup = BeautifulSoup(page.content, 'html.parser')
    genre_find = soup.find("div", {"id": 'genresAndManufacturer'})
    descr_find = soup.find_all("div", class_='game_description_snippet')
    print(descr_find)
    write_descr = ""
    for descr in descr_find:
        write_descr += descr.text.strip()
        print(write_descr)
    
    if (genre_find is not None) and (write_descr != "Steam is the ultimate destination for playing, discussing, and creating games."):
        genre = genre_find.findNext("a").text.strip()
        write_file.write(p_name + '|' + p_id.strip() + '|' + genre + '|' + write_descr + '\n')
    write_file.close()

def main():
    id_file = open('id_mappings.txt', 'r', encoding='utf-8')

    game_names = []
    game_ids = []
    game_attr = []
    for line in id_file:
        if line == '':
            continue
        elif line == '+':
            continue

        game_name = line.split(',')[0].strip()
        game_id = line.split(',')[1].strip()

        game_names.append(game_name)
        game_ids.append(game_id)
        game_attr.append([game_name, game_id])
    with Pool(10) as p:
        p.starmap(scrape_page, game_attr)

    id_file.close()

if __name__=="__main__":
    freeze_support()
    main()