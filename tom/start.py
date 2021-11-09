import steamScrape

scrapeList = open('tom_filtered.txt', 'r', encoding='utf-8')
# scrapeResults = open('scrapeResults.csv', 'w+') # '+' allows creation of file if not existing
scrapeResults = open('scrapeResults.csv', 'a+') # '+' allows creation of file if not existing
scrapeResume = open('resume.txt', 'r')

resume = scrapeResume.readline()
resumeArr = resume.split(',')
rowNumResume = resumeArr[0]
lineNumResume = resumeArr[1]

# set file pointer to correct line number to start reading from.
scrapeList.seek(lineNumResume)


# NOTE: do I multiprocess "steamScrape()"??
# If so: does multiprocess stuff in python lockout files properly while reading/writing them?
# NOTE: Doing multiprocess makes resuming VERY challenging

steamScrape(scrapeList, scrapeResults, rowNumResume, lineNumResume)

scrapeResults.close()
scrapeList.close()