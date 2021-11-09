from bs4 import BeautifulSoup
import requests
import csv

# extracts data from steam game pages and stores it in csv file
# "scrapeList" contains game names and ids to be scraped
# "scrapeResults" references the csv file to store results
# "scrapeResume" is the file containing the "rowNumResume, lineNumResume"
# "rowNumResume" is the row number in the csv file to start writing to
# "lineNumResume" is the line number in scrapeList file to start reading from
def steamScrape(scrapeList, scrapeResults, scrapeResume, rowNumResume, lineNumResume):
    
    # test code
    testI = 1

    for line in scrapeList:
        
        # test code
        if testI == 5: exit()
        else: testI += 1
        print(line)

        # add 1 to start on correct line number of scapeList file
        lineNumResume += 1

        # process line: separating game name from game id, and tracking file line number
        if lineNumResume 
        elif line == '':
            continue
        elif line == '+':
            continue
        game_name = line.split(',')[0]
        game_id = line.split(',')[1]
        print(game_name + ', ' + game_id)
        
        # 
        #https://store.steampowered.com/app/1690670
        URL = 'https://store.steampowered.com/app/' + game_id
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        tags = soup.find_all(class_='app_tag')
        # price = 
        # genre = 

        if tags is None:
            continue

        for tag in tags:
            if tag == '':
                continue
            
            scrapeResults.writerow([game_id, game_name, tag])
            rowNumResume += 1


        # ###################################################################################
        # recommended_table = soup.find(class_='game_area_sys_req_rightCol')

        # if recommended_table is None:
        #     continue

        # recommendeds = recommended_table.find_all(class_='bb_ul')

        # for recommended in recommendeds:
        #     if recommended == '':
        #         continue

        #     # only one WRITE statement ensures we know what/when we write to scrapeResults file
        #     scrapeResults.write\
        #     (\
        #         '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'\
        #         + game_name + ', ' + game_id\
        #         + recommended.text.strip()+'\n'\
        #     )

        #     print\
        #     (\
        #         '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'\
        #         + game_name + ', ' + game_id\
        #         + recommended.text.strip()+'\n'\
        #     )

        #     # scrapeResults.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        #     #scrapeResults.write(game_name + ', ' + game_id)
        #     #scrapeResults.write(recommended.text.strip()+'\n')
