'''
set_andrew_channel.py
'''

import os
from discord.ext import commands

from config import ADM_USERS # fix if needed


@commands.command()
async def set_channel(ctx, arg=None):
    '''
    Set optional ANDREW_CHANNEL for ping command.
    [ADMIN COMMAND]
    '''

    if ctx.author.id not in ADM_USERS:
        return
    
    await ctx.message.delete()

    prefix = "ANDREW_CHANNEL = "

    try:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(file_dir, "../config.py")

        with open(config_path, "r") as f:
            lines = f.readlines()

        with open(config_path, "w") as f:
            for line in lines:
                if line.startswith(prefix):
                    if arg is not None:
                        f.write(f"{prefix}{arg}\n")
                    else:
                        current_channel = ctx.channel.id
                        f.write(f"{prefix}{current_channel}\n")
                else:
                    f.write(line)
    except Exception as e:
        print(e)

    await ctx.send(":thumbsup:")