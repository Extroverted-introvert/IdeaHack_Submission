import tweepy


def get_tweet_sentiment(city, query):
        
    auth = tweepy.OAuthHandler("sWHOzqDwM3UbT7XqQcKvR2wku", "t2OYKAbry0knI1VSaWLtOTsE18dqiE0yQdc6kwIFg5wj9TRJ8U")
    auth.set_access_token("810538727944704000-r5YCr88V4A86dUbJx0fl9I02sPRee86", "cWWmdGCuVrPjNQb3hI5dwijmb4Z7l3Us4yjGv8CsGJHx3")

    api = tweepy.API(auth)
    try:
        places = api.geo_search(query=city, granularity="city")
    except:
        places = api.geo_search(query="Delhi", granularity="city")    
    place_id = places[0].id
    
    tweets = api.search(q="{} place:{}".format(query,place_id), tweet_mode="extended")
    return tweets