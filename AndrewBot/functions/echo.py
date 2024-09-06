'''
echo.py
'''

from discord.ext import commands

@commands.command()
async def echo(ctx, *, msg):
    '''
    Echos the provided message.
    '''
    
    await ctx.send(msg)