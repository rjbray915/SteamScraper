#Filter for game titles to remove NSFW content
def filter_titles(fn):
    FILTER_LIST = ['18+', 'sex', 'fuck', 'hentai', 'dick', 'shit', 'cock', 'cum']
    with open(fn, 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    for i in range(len(data)):
        data[i] = data[i].lower()
        print(data[i])
    
    l = []
    for d in data:
        for f in FILTER_LIST:
             if f not in d:
                 l.append([d])
                 break
    x = []
    for d in data:
        for f in FILTER_LIST:
             if f in d:
                 x.append([d])
                 break
    print(len(x))
    print(len(l))
    with open('SteamScraper/filtered.txt', 'w', encoding='utf-8') as f:
        for i in l:
            f.write(i[0])


filter_titles("SteamScraper/id_mappings.txt")