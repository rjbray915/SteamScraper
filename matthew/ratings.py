from bs4 import BeautifulSoup
import requests
import multiprocessing as mp



def rating(game_name, game_id):
    rating_file = open('test_rating.txt', 'a', encoding='utf-8')
    URL = 'https://store.steampowered.com/app/' + game_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    rating_table = soup.find(class_='summary_section')
    if rating_table is None:
        return
    rating = rating_table.find_all(class_="game_review_summary positive")

    if len(rating) == 0:
        rating = rating_table.find_all(class_="game_review_summary")    
    rating_file.write(game_name + ', ' + game_id + ", " + rating[0].text.strip())
 
    rating_file.write('\n')
    rating_file.close()

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
        p.starmap(rating, arguments)
    id_file.close()

if __name__ == "__main__":
    main()
