from django.shortcuts import render
from custom_sentiment_fetch.apps import CustomSentimentFetchConfig
from custom_sentiment_fetch.twitter_api2 import get_tweet_sentiment
import numpy as np

# Create your views here.
def custom_sentiment(request):
    context = {}
    print(request.method)
    
    if request.method == 'GET':
        return render(request, 'custom_sentiment/custom_sentiment.html', context)
    
    elif request.method == 'POST':
        city = request.POST['city']
        query = request.POST['query']
        prediction_list =[]
        tweets = get_tweet_sentiment(city, query)
        for tweet in tweets:
            prepared_text=np.array([tweet.full_text])
            prediction_score = np.float64(CustomSentimentFetchConfig.sentiment_model.predict(prepared_text)[0][0]).item()
            prediction_list.append(prediction_score)
        if len(prediction_list) >0:
            final_score = sum(prediction_list)/len(prediction_list)    
            prediction = assign_prediction(final_score)
            final_list = tuple(zip(tweets, prediction_list)) 
            context ={'sentiment':prediction, 'sentiment_score':final_score, 'tweet_list': final_list}
            return render(request, 'custom_sentiment/custom_sentiment.html', context)
        else:
            context = {'error': "Sorry, Unable to perform analysis for given parameters"}
            return render(request, 'custom_sentiment/custom_sentiment.html', context)   

def assign_prediction(prediction_score):
        pred_score=prediction_score
        sentiment = 'Negative'
        if(pred_score<-0.5):
            sentimentg = 'Poor'
        elif(pred_score>=-0.5 and pred_score<0.5):
            sentiment = 'Average'
        elif(pred_score>=0.5 and pred_score<1):
            sentiment = 'Good'
        elif(pred_score>=1):
            sentiment = 'Positive' 
        return sentiment