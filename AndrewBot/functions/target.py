'''
target.py
'''

import os
from discord.ext import commands

from config import ADM_USERS

# Target
@commands.command()
async def target(ctx, arg=None):
    '''
    Selects a target for AndrewBot
    [ADMIN COMMAND]
    '''
    
    new_ID = arg.translate(str.maketrans('', '', '<>@'))

    if ctx.author.id not in ADM_USERS:
        return

    prefix = "ANDREW_ID = "

    try:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(file_dir, "../config.py")

        with open(config_path, "r") as f:
            lines = f.readlines()

        with open(config_path, "w") as f:
            for line in lines:
                if line.startswith(prefix):
                    if arg is not None:
                        f.write(f"{prefix}{new_ID}\n")
                    else:
                        ctx.send("Choose target: [$target <@user>].")
                else:
                    f.write(line)
    except Exception as e:
        print(e)

    await ctx.send(":thumbsup:")