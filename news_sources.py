import pandas as pd

df  = pd.read_csv("new_websites.csv")

trustworthy = df[:15]
untrustowrthy = df[15:]

print trustworthy

print untrustowrthy
# print df.all()