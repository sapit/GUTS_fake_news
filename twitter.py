import tweepy
import requests
import re
import pandas as pd
from urlparse import urlparse
from google_crawl import google_get_result_links

twitter_app_auth = {
    'consumer_key': '2NVO6JJl1Yig7XXuKMoa2PSkl',
    'consumer_secret': 'c9H6PAY9io3IlU3P3H44wihWCX80Ngo25d0RNGDWwGR9Zn6Utn',
    'access_token': '3131597903-eJp1XGXfXJj3iTnPYT0k50chm5p7RMCrZJJPPjG',
    'access_token_secret': 'Wo3iZaFhtDmdhHCAZNjYjFzjf14XwRb8ak93Qd0nVc1Dj',
  }

auth = tweepy.OAuthHandler(twitter_app_auth["consumer_key"], twitter_app_auth["consumer_secret"])
auth.set_access_token(twitter_app_auth["access_token"], twitter_app_auth["access_token_secret"])

df  = pd.read_csv("new_websites.csv")
trustworthy = df[:15]
untrustowrthy = df[15:]


api = tweepy.API(auth)

public_tweets = api.home_timeline()



username = '@guardian'

def normalize_url():
  pass

new_tweets = api.user_timeline(screen_name = username,count=20)
print trustworthy["URL"]
for i in range(len(new_tweets)):

    trustworthy_links_in_tweet = []
    untrustworthy_links_in_tweet = []
    unknown_links_in_tweet = []

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', new_tweets[i].text)
    # print urls
    trustworthy_urls = list(trustworthy["URL"])
    untrustworthy_urls = list(trustworthy["URL"])

    for t in range(len(trustworthy_urls)):
        trustworthy_urls[t] = trustworthy_urls[t].replace("http://","")
        trustworthy_urls[t] = trustworthy_urls[t].replace("https://","")
        trustworthy_urls[t] = trustworthy_urls[t].replace("www.","")
    # for j in range(len(trustworthy_urls)):
    #     trustworthy_urls[j] = 
    if(urls):
      for u in urls:
          new_tweets[i].text = new_tweets[i].text.replace(u,"")
          r = requests.get(u)

          parsed_uri = urlparse(r.url)
          domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

          domain = domain.replace("http://","")
          domain = domain.replace("https://","")
          domain = domain.replace("www.","")


          if(domain in trustworthy_urls):
              trustworthy_links_in_tweet.append(domain)
          elif(domain in untrustowrthy):
              untrustworthy_links_in_tweet.append(domain)
          else:
              unknown_links_in_tweet.append(domain)

    
    # result_links = google_get_result_links(new_tweets[i].text)
    result_links = google_get_result_links(new_tweets[i].text)
    for t in range(len(result_links)):
        result_links[t] = result_links[t].replace("http://","")
        result_links[t] = result_links[t].replace("https://","")
        result_links[t] = result_links[t].replace("www.","")
    
    print "res links ", result_links
    print "trustworthy urls ", trustworthy_urls
    if(result_links):
        print result_links[0] in trustworthy_urls
    
    matching_trustworthy_urls = []
    matching_untrustworthy_urls = []
    unknown_urls = []

    for l in result_links:
        if l in trustworthy_urls:
            matching_trustworthy_urls.append(l)
        elif l in untrustworthy_urls:
            matching_untrustworthy_urls.append(l)
        else:
            unknown_urls.append(l)
    # matching_trustworthy_urls = ["TRUSTWORTHY" for l in result_links if l in trustworthy_urls]
    
    print trustworthy_links_in_tweet
    print untrustworthy_links_in_tweet
    print unknown_links_in_tweet
    
    print matching_trustworthy_urls
    print matching_untrustworthy_urls
    print unknown_urls
      # if(domain in list(trustworthy["URL"])):
      #     print "TRUSTWORTHY"
    # print dir(new_tweets[i])
    print "new_tweets[i].text ", new_tweets[i].text
    # print "new_tweets[i].source ", new_tweets[i].source
    # print "new_tweets[i].source_url ", new_tweets[i].source_url
    # print "new_tweets[i].possibly_sensitive ", new_tweets[i].possibly_sensitive
    # print "new_tweets[i].author ", new_tweets[i].author
    # print "new_tweets[i].user ", new_tweets[i].user
    # print "new_tweets[i].truncated ", new_tweets[i].truncated


# print dir(user)
# for tweet in public_tweets:
#     print tweet.text
#     urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.text)
#     print urls



