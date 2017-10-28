import pandas as pd

df  = pd.read_csv("fake.csv")
# print df.info()

print df['spam_score']
