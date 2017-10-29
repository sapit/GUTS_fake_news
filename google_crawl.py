google_api_key = "AIzaSyCNOjl3325kaVW1ggkaBRUTOfrVU_w5fi8"
google_cse = "013423243973335134068:mkdiyxdnke8"

from googleapiclient.discovery import build


def google_get_result_links(query):
    service = build("customsearch", "v1",
                    developerKey=google_api_key)

    result = service.cse().list(
            q=query,
            cx=google_cse
        ).execute()
    # result = result[:5]
    # print result.keys()
    # print result['kind']
    # try:
    #     print result["items"][0].keys()
    # except:
    #     return []

    links = []
    for i in range(min(len(result['items']), 5)):
        # print result["items"][i]['title']
        # print result["items"][i]['snippet']
        # print result["items"][i]['link']
        # print result["items"][i]['displayLink']
        l = result["items"][i]['displayLink'].encode("utf-8")
        if l[len(l)-1] != '/':
            l+='/'
        links.append(l)
        
    # return result["searchInformation"]["totalResults"]
    return links

if __name__=="__main__":
    q = "Bootsy Collins: LSD was a big part of why I left James Browns band"
    # print google_get_result_links(q)