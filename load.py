import pandas as pd
import json 
df  = pd.read_csv("fake.csv")
# print df.info()

print list(df)
# print df['text'][0]
df['title']
df['text']

df = df[df['language'].str.contains("english")]

df1 = df[['title','text']]
print df1


# df2 = pd.read_json("660_webhose-2015-10-new_20170904095249/news_0000001.json")
# print df2
# with open('660_webhose-2015-10-new_20170904095249/news_0000010.json') as data_file:
#     data = json.load(data_file)
#     print data.keys()
#     print data['title']
#     print data['text']
#     print data['entities']
bbc=[]
folders = ['business', 'entertainment', 'politics']
for folder in folders:
    for i in range(1,300):
        with open("bbc/%s/%s.txt"%(folder, str(i).zfill(3))) as data_file:
            title = data_file.readline()
            content = ""
            line = data_file.readline()
            while(line):
                line=line.strip()
                if(line):
                    content+=line
                line = data_file.readline()
            bbc.append((title,content))
print len(bbc)

