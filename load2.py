# import numpy as np
# import csv

# import numpy as np
# csv = np.genfromtxt('fake.csv', delimiter=",")
# print csv

# # import csv
# # with open('fake.csv', newline='') as f:
# #     csvread = csv.reader(f)
# #     batch_data = list(csvread)
# #     print batch_data


import pandas as pd
import numpy as np
import spacy
import scattertext as st
#import imp; imp.reload(st)
# from IPython.display import IFrame
# from IPython.core.display import display, HTML
# display(HTML("<style>.container { width:98% !important; }</style>"))
import pickle
from nltk.corpus import reuters
# %matplotlib inline  

nlp = spacy.en.English()

uci_df = pd.read_csv('uci-news-aggregator.csv.gz')
# print (uci_df)
traditional_publishers = ['Forbes','Bloomberg','Los Angeles Times','TIME','Wall Street Journal']
repubable_celebrity_gossip = ['TheCelebrityCafe.com', 'PerezHilton.com']
real_df = uci_df[uci_df['PUBLISHER'].isin(traditional_publishers)]
real_df.columns = [x.lower() for x in real_df.columns]
real_df['type'] = 'traditional'

df = pd.read_csv('fake.csv')
df = df.append(real_df)
df = df[df['title'].apply(lambda x: type(x) == str)]
df['clean_title'] = df['title'].apply(lambda x: ' '.join(x.split('»')[0].split('>>')[0].split('[')[0].split('(')[0].split('|')[0].strip().split()))
df = df.ix[df['clean_title'].drop_duplicates().index]
df['parsed_title'] = df['clean_title'].apply(nlp)
df['meta'] = df['author'].fillna('') + df['publisher'].fillna('') + ' ' + df['site_url'].fillna('')
df['category'] = df['type'].apply(lambda x: 'Real' if x == 'traditional' else 'Fake')
fake_df = df[df['category'] == 'Fake']

print (fake_df.type.value_counts())