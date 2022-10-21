import random
import tweepy
from pygelbooru import Gelbooru
import os

developer = False

blacklist = ['gore', 'rape', 'futa', 'loli', 'guro', 'snuff', 'amputation', 'pregnant']
 
# API keyws that yous saved earlier
bearer_token = os.environ['bearer_token']

# Authenticate to Twitter
tclient = tweepy.Client(bearer_token)

# gets specified user
user_id = os.environ['twit_user_id']

# hello gelbooru
gelbooru = Gelbooru('gel_api_key', 'gel_id_key')

#empty variables
tweet_list = []
tosendprevious = ''

async def handle_response(message) -> str:
  p_message = message.lower()
  global developer
  if p_message == '!developermodeasuna':
    developer = True
    return 'debug mode activated'

  if p_message == '!goodbye':
    developer = False
    return 'see you next time'

  if p_message == '!s':
    response = tclient.get_liked_tweets(user_id, tweet_fields =["entities"], max_results=100)
    for tweet in response.data:
      tweets = tweet.id, tweet.entities
      tweet_list.append(tweets)
    liked_post = random.choice(tweet_list)
    first = liked_post[1]
    second = first.get('urls')
    third = second[0]
    return third.get('expanded_url')

  if p_message == '!gel':
    msgcontent = p_message.replace('!gel', ' ')
    search2 = msgcontent.strip()
    results = await gelbooru.random_post(tags=search2, exclude_tags=blacklist)
    if not results:
      return 'no results found!!!'
    else:
      return results

  if p_message == '!helpme':
    return '!s - spits out random liked posts from krisnards twitter account\n!gel (tags) - searches random gelbooru image with the specified tags. if no results are found use different variations. multiple tags allowed. if no tags specified, it will spit out a completely random image'