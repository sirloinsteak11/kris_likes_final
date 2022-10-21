import os
import discord
from discord.ext import commands
import responses

bot = commands.Bot(command_prefix='!', case_insensitive=True)

bot.author_id = 302320256586612737


async def send_message(message, user_message):
  try:
    response = responses.handle_response(user_message)
    await message.channel.send(response)

  except Exception as e:
    print(e)


def run_discord_bot():
  TOKEN = os.environ['bot_token']
  client = discord.Client()

  @client.event
  async def on_ready():
    print(f'{client.user} has connected to Discord!')

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    # Debug printing
    print(f"{username} said: '{user_message}' ({channel})")

    await send_message(message, user_message)

  client.run(TOKEN)
