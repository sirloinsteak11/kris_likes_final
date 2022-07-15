# bot.py
import os
import random
import tweepy

import discord
from dotenv import load_dotenv

from discord.ext import commands

TOKEN = os.environ['BOT_TOKEN']

intents = discord.Intents.default()
intents.members = True # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='!', intents=intents)
intents.typing = True # allows bot to type????
intents.messages = True # allows bot to connect to messages?!!?!?!?!
 
# API keyws that yous saved earlier
bearer_token = "AAAAAAAAAAAAAAAAAAAAABxHdwEAAAAAtx%2Bz2PRL%2F54wEmMvzU8QMHcR3Wo%3DqfxCoUvGU1xM88vSEKYJQMxUIhy1pASQZabWmMaYpPYugOqT9S"

# Authenticate to Twitter
tclient = tweepy.Client(bearer_token)

# gets specified user
user_id = '1334974466049204226'

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

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

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
    
    if message.content == '!helpme':
        await message.channel.send('!s - my only command. spits out random liked posts from krisnards twitter account')

client.run(TOKEN)