from nytimesarticle import articleAPI

def nyt_scrape():
    api = articleAPI('9c3c5c7def7d4023a9a8a3193f8ed585')
    articles = api.search( q = 'Obama', 
        fq = {'headline':'Obama', 'source':['Reuters','AP', 'The New York Times']}, 
        begin_date = 20111231 )
    def parse_articles(articles):
        '''
        This function takes in a response to the NYT api and parses
        the articles into a list of dictionaries
        '''
        news = []
        print articles
        for i in articles['response']['docs']:
            dic = {}
            dic['id'] = i['_id']
            print i.keys()
            # print i['snippet']
            # print i
            if i['snippet'] is not None:
                dic['snippet'] = i['snippet'].encode("utf8")
            dic['headline'] = i['headline']['main'].encode("utf8")
            dic['desk'] = i['news_desk']
            dic['date'] = i['pub_date'][0:10] # cutting time of day.
            dic['section'] = i['section_name']
            if i['snippet'] is not None:
                dic['snippet'] = i['snippet'].encode("utf8")
            dic['source'] = i['source']
            dic['type'] = i['type_of_material']
            dic['url'] = i['web_url']
            dic['word_count'] = i['word_count']
            # locations
            locations = []
            for x in range(0,len(i['keywords'])):
                if 'glocations' in i['keywords'][x]['name']:
                    locations.append(i['keywords'][x]['value'])
            dic['locations'] = locations
            # subject
            subjects = []
            for x in range(0,len(i['keywords'])):
                if 'subject' in i['keywords'][x]['name']:
                    subjects.append(i['keywords'][x]['value'])
            dic['subjects'] = subjects   
            news.append(dic)
        return(news) 

    x = parse_articles(articles)
    print x

nyt_scrape()