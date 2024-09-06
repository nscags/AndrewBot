'''
history.py
'''

from time import time
from random import choice
from datetime import datetime
import json
import os
import discord
from discord.ext import commands

# from .refresh import refresh_channel_cache

# TODO: display images/gifs (currently just displays the link)
#       theres probably a way to do this with embeds but will need to check message type maybe?

@commands.command()
async def history(ctx, userID=None):
    '''
    Selects a random message from the channel's history.
    '''

    await ctx.message.delete()

    start = time()

    file_path = os.path.dirname(os.path.abspath(__file__))
    channel_id = ctx.message.channel.id
    pattern = f'{channel_id}_'

    matching_files = []

    # List all files in the directory
    files_in_directory = os.listdir(os.path.join(file_path, 'channel_cache'))

    # Filter files based on the pattern
    matching_files = [file for file in files_in_directory if pattern in file]

    if matching_files:
        # Assuming you want to work with the first matching file
        file_name = matching_files[0]
        file_path = os.path.join(file_path, 'channel_cache', file_name)
        try:
            with open(file_path, 'r') as f:
                data = f.read()
            channel_history = json.loads(data)
        except Exception as e:
            channel_history = None
            print(f'Error: {e}')
            return
    else:
        # TODO: If there is no cache, create a new one
        # for rn just ping me and I'll create one
        # await refresh_channel_cache(ctx)
        await ctx.send(f'<@{496372315848966147}>')
        return
        

    # Prase messages
    total_messages = channel_history[-1]['number']
    message = choice(channel_history)
    if userID is not None: 
        userID = int(userID[2:-1])
        while message['author']['id'] != userID:
            message = choice(channel_history)
    message_content = message['content']
    messageID = message['id']
    message_datetime = message['created_at']
    fmessage_datetime = datetime.fromisoformat(message_datetime).strftime("%m-%d-%Y %H:%M")

    guild = ctx.guild
    member = guild.get_member(message['author']['id'])

    # Embed Formatting
    color = member.top_role.color
    pfp = member.avatar
    name = f'{member.display_name} ({member.name})'

    embed = discord.Embed(color=color, description=message_content)
    embed.set_author(name=name, icon_url=(pfp))
    end = time()
    time_elapsed = round(end - start, 2)
    print(time_elapsed)
    embed.set_footer(text='MessageID: ' + str(messageID) + '  |  ' + str(fmessage_datetime) + f'\nTime Elapsed: {time_elapsed}s  |  Total Messages: {total_messages}' )

    await ctx.send(embed=embed)