# bot.py
import os
import random
import tweepy
from pygelbooru import Gelbooru
import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='!', intents=intents)
intents.typing = True # allows bot to type
intents.messages = True # allows bot to connect to messages?!!?!?!?!
 
# API keyws that yous saved earlier
bearer_token = os.getenv('BEARER_TOKEN')

# Authenticate to Twitter
tclient = tweepy.Client(bearer_token)

# gets specified user
user_id = os.getenv('USER_ID')

# hello gelbooru
gelbooru = ('GEL_API_KEY', 'GEL_ID_KEY')

#empty variables
tweet_list = []
tosendprevious = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!s':
        response = tclient.get_liked_tweets(user_id, tweet_fields=["entities"], max_results=100)
        for tweet in response.data:
            tweets = tweet.id, tweet.entities
            tweet_list.append(tweets)
        liked_post = random.choice(tweet_list)
        first = liked_post[1]
        second = first.get('urls')
        third = second[0]
        tosend = third.get('expanded_url')
        await message.channel.send(tosend)
        await message.channel.send("enjoy :grin:")

    if '!gel' in message.content:
        msgcontent = message.content
        search = msgcontent.replace('!gel', '')
        results = await gelbooru.search_posts(search.split(','))
        tosend = results[0]
        await message.channel.send(tosend)
        await message.channel.send(search)
    
    if message.content == '!helpme':
        await message.channel.send('!s - my only command. spits out random liked posts from krisnards twitter account')

client.run(TOKEN)