'''
client.py
'''

from discord import Intents 
from discord.ext import commands

# Define intents and create bot
intents = Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
# Change only the no_category default string
help_command = commands.DefaultHelpCommand(no_category = 'Commands')
client = commands.Bot(command_prefix='$', intents=intents, help_command=help_command)