import discord as dis
import random as r
import os
from dotenv import load_dotenv

load_dotenv()
bot = dis.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")

@bot.slash_command(name = "char-creation", description = "Create your SwordWorld 2.5 character.")
async def char_create(ctx):
    pass

bot.run(os.getenv('TOKEN'))