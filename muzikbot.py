from lib2to3.pgen2 import token
import discord
from discord.ext import commands
from music import *

cogs = [music]

client = commands.Bot(command_prefix=">", intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTYwMTc4MTU2OTQ4NTc0MjQ4.Ykmplw.VmWUmPE64I8ejywQPDiSUZfc5ew")