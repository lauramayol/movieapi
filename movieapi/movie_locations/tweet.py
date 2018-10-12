import tweepy
import os


class Trends:

    def set_tweep_connection(self):
        consumer_key = os.environ["TWITTER_API_KEY"]
        consumer_secret = os.environ["TWITTER_API_SECRET_KEY"]
        access_token = os.environ["TWITTER_ACCESS_TOKEN"]
        access_token_secret = os.environ["TWITTER_ACCESS_SECRET"]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        return api

    def get_location_trends(self, api, clat, clong):
        '''
            Variables:
            api (object) = tweepy api connection with twitter.
            clat (float) = latitude of location we are searching for.
            clong (float) = longitude of location we are searching for.

            Return Value:
            Returns nearest location details and its most current top 10 trends in Twitter.
        '''

        closest_locations = api.trends_closest(clat, clong)

        # Get the first closest location in Twitter based on clat, clong. Tweepy already sorts by closest first.
        for i in range(1):
            twitter_location = closest_locations[i]

        return_value = {"NearestLocation": twitter_location}

        # Get the top 10 trends according to twitter_location, sorted by tweet_volume (max first).
        top_trends = api.trends_place(twitter_location['woeid'])[0]['trends']
        top_trends = sorted(top_trends, key=lambda dict: dict['tweet_volume'] or 0, reverse=True)

        t = top_trends[:10]
        top10 = list()
        for i, val in enumerate(t, start=1):
            tup = i, val
            top10.append(tup)

        return_value["Top10Trends"] = top10
        return return_value
