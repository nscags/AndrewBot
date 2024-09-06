'''
ping.py
'''

from discord.ext import commands
from config import ANDREW_ID, ANDREW_CHANNEL, ADM_USERS
from client import client
from time import sleep

stop_flag = False

# Ping
@commands.command()
async def ping(ctx, num = 1, *,args = ''):
    '''
    Pings Andrew
    '''
    global stop_flag
    stop_flag = False

    # delete message calling the command
    await ctx.message.delete()

    # Get andrew channel id, raise error if cannot find
    andrew_channel = client.get_channel(ANDREW_CHANNEL)
    if andrew_channel is None: 
        await ctx.send("Error: Unable to get channel.")
        return

    # Ping Andrew x amount of times
    while num > 0 and not stop_flag:
        await andrew_channel.send("<@" + str(ANDREW_ID) + ">" + ' ' + args)
        num -= 1
        sleep(1)



# TODO: fix the stop command
# Stop
@commands.command()
async def stop(ctx):
    '''
    Stops the ping command
    [Admin Command]
    '''
    if ctx.author.id not in ADM_USERS:
        return
    
    await ctx.message.delete()

    global stop_flag
    stop_flag = True    