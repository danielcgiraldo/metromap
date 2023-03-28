import snscrape.modules.twitter as st

def gettweets(num = 5):
    '''Obtiene los ultimos 5 tweets del metro de medellin'''
    
    # Excluir las respuestas y solo filtrar ultimos tweets
    query = "(from:metrodemedellin) -filter:replies"
    tweets = {"status":"okay", "data":[]}
    # Se obtienen los tweets del objeto creado por twitterSearchScrapper
    for i,t in enumerate(st.TwitterSearchScraper(query).get_items()):
        
        # Filtrar exclusivamente la descripcion del tweet
        cleanup = t.rawContent
        cleanup = cleanup.replace("\n",'')
        # Se agregan el ID, URL, Descripcion del tweet
        if i < num: tweets["data"].append({"id":t.id, "url":t.url, "content":cleanup})
        else: break

    # Retorna un diccionario con el estado y el ID, URL, Descripcion de los tweets
    return tweets