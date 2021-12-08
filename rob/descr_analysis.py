import re, operator
from collections import Counter
from os import error
import pandas as pd
import csv
import numpy as np
from pattern.text.en import singularize
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag
from matplotlib import pyplot as plt
import pylab

def plotProp (wf_ee, title, prefix):
    plt.subplots_adjust(left=.3)
    pos = np .arange (len(wf_ee)) 
    pylab .yticks (pos, [ x [0] for x in wf_ee ])
    plt.barh (range(len(wf_ee)), [ x [1] for x in wf_ee ], align='center', color='purple')
    plt.title('Proportion of: ' + title)
    plt.xlabel('Proportion of Total Words')
    plt.savefig(prefix+title)
    plt.clf()

df = pd.read_csv('test_genre_descr.csv', delimiter='|', error_bad_lines=False, quoting=3)

#dictionary to hold each genre
genre_words = {'Casual' : [], 
                'Action': [],
                'Simulation': [],
                'RPG': [],
                'Indie': [],
                'Adventure': [],
                'Massively Multiplayer' : [],
                }
genre_descrs = {'Casual' : "",
                'Action': "",
                'Simulation': "",
                'RPG': "",
                'Indie': "",
                'Adventure': "",
                'Massively Multiplayer' : "",
                }
genre_total_counts = {'Casual' : 0,
                'Action': 0,
                'Simulation': 0,
                'RPG': 0,
                'Indie': 0,
                'Adventure': 0,
                'Massively Multiplayer' : 0,
                }

# these are the words we want to ignore
filter_words = ['game', ''] + stopwords.words('english')

# split up words into array
for i in range(np.size(df['description'])):
    test_descr = df['description'][i]
    if pd.isna(test_descr):
        continue

    # # append description
    # try:
    #     genre_descrs[df['genre'][i]] += test_descr
    # except:
    #     genre_descrs[df['genre'][i]] = ''
    #     genre_descrs[df['genre'][i]] += test_descr

    # clean up the words
    test_descr = test_descr.lower()
    wds = re.split('\s+', test_descr)
    for j in range(len(wds)):
        wds[j] = re.sub('[,"\.\'&\|:@>*;/=!?.()-]', "", wds[j])

    # add the words to the corresponding list
    try:
        genre_words[df['genre'][i]] += (wds)
    except:
        genre_words[df['genre'][i]] = []
        genre_words[df['genre'][i]] += (wds)


real_genres = ['Casual', 'Action', 'Simulation', 'RPG', 'Indie',
                'Adventure', 'Massively Multiplayer', 'Sports',
                'Free to Play', 'Strategy', 'Education',
                'Early Access', 'Racing']
genres_counted = {}

for key in real_genres:
    # save number of words
    genre_total_counts[key] = len(genre_words[key])
    print(genre_total_counts)

genre_new = []
genre_world = []
genre_play = []
genre_verbs = []
genre_adjectives = []
genre_nouns = []
genre_foreign = []
for key in real_genres:

    # for most-used types of words
    tokenized = pos_tag(genre_words[key])
    tags_counted = list(Counter([j for i,j in pos_tag(genre_words[key])]).items())
    print(key, tags_counted)

    # for most-used words
    genres_counted[key] = Counter(genre_words[key])
    for wd in filter_words:
        genres_counted[key].pop(wd, None)
    wfs = sorted (genres_counted[key].items(), key = operator.itemgetter(1), reverse=True)
    plotProp(wfs[0:10], key, 'descr_')
    print(key, wfs[0:10])

    # make word-specific ratios
    interest_words = ['new', 'world', 'play']
    
    genre_new.append((key, list(filter(lambda i:'new' in i, wfs))[0][1] / genre_total_counts[key]))
    print(genre_new) 
    genre_world.append((key, list(filter(lambda i:'world' in i, wfs))[0][1] / genre_total_counts[key]))
    print(genre_world)
    genre_play.append((key, list(filter(lambda i:'play' in i, wfs))[0][1] / genre_total_counts[key]))
    print(genre_play)
    genre_verbs.append((key, list(filter(lambda i:'VB' in i, tags_counted))[0][1] / genre_total_counts[key]))
    print(genre_verbs)
    genre_adjectives.append((key, list(filter(lambda i:'JJ' in i, tags_counted))[0][1] / genre_total_counts[key]))
    print(genre_verbs)
    genre_nouns.append((key, list(filter(lambda i:'NN' in i, tags_counted))[0][1] / genre_total_counts[key]))
    print(genre_nouns)

plotProp(genre_new, 'New', 'prop_')
plotProp(genre_world, 'World', 'prop_')
plotProp(genre_play, 'Play', 'prop_')
plotProp(genre_verbs, 'Verbs', 'prop_')
plotProp(genre_nouns, 'Nouns', 'prop_')
plotProp(genre_adjectives, 'Adjectives', 'prop_')