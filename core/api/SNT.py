import snscrape.modules.twitter as st
import json

def gettweets(num=5):
    query = "(from:metrodemedellin) -filter:replies"
    tweets = {"status":"okay", "data":[]}
    for i,t in enumerate(st.TwitterSearchScraper(query).get_items()):
        cleanup = t.rawContent
        # cleanup = cleanup[ 0 : t.content.index("https")]
        cleanup = cleanup.replace("\n",'')
        if i < num: tweets["data"].append({"id":t.id, "url":t.url, "content":cleanup})
        else: break

    #turned into json
    output = json.dumps(tweets, ensure_ascii=False)
    return output
    




# import os

# # Using OS library to call CLI commands in Python
# os.system("snscrape --jsonl --max-results 5 twitter-user metrodemedellin> metromapTweets.json")