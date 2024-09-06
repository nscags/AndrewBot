from datetime import datetime
import json
import os
import glob
from discord.ext import commands

from config import ADM_USERS


class Message():
    def __init__(self, id):
        self.id = id

@commands.command(name='refresh')
async def refresh_channel_cache(ctx):
    '''
    Creates a cache of all the messages in a channel's history. 
    [ADMIN COMMAND]
    '''
    await ctx.message.delete()

    if ctx.message.author.id not in ADM_USERS:
        print("Invalid userID.")
        return

    try:
        channel_id = ctx.message.channel.id
        file_path = os.path.dirname(os.path.abspath(__file__))
        pattern = f'{file_path}/channel_cache/{channel_id}_*'
        current_date = datetime.today().strftime('%Y%m%d')
        channel_cache = glob.glob(pattern)

        if channel_cache:
            channel_cache = channel_cache[0] 
            
            with open(channel_cache, 'r+') as f:
                data = f.read()
                channel_history = json.loads(data)
                last_message = channel_history[-1]
                last_message_id = last_message['id']
                count = last_message['number']
                
                last_message_obj = Message(last_message_id)

                f.seek(0, os.SEEK_END)
                pos = f.tell()
                f.seek(pos - 1)
                f.truncate()
                
                async for message in ctx.channel.history(limit=None, oldest_first=True, after=last_message_obj):
                    f.write(',\n')
                    message_data = {
                        'id': message.id,
                        'author': {
                            'id': message.author.id,
                            'name': str(message.author.name),
                            'display_name': message.author.display_name
                        },
                        'content': message.content,
                        'created_at': str(message.created_at),
                        'number': count
                    }
                    json.dump(message_data, f, indent=4)
                    count += 1
                f.write("]")

            os.rename(channel_cache, f'{file_path}/channel_cache/{channel_id}_{current_date}.json')
        else:
            with open(f'{file_path}/channel_cache/{channel_id}_{current_date}.json', 'w') as f:
                f.write("[") 
                count = 0
                async for message in ctx.channel.history(limit=None, oldest_first=True):
                    if count > 0:
                        f.write(',')
                        f.write('\n')
                    message_data = {
                        'id': message.id,
                        'author': {
                            'id': message.author.id,
                            'name': str(message.author.name),
                            'display_name': message.author.display_name
                        },
                        'content': message.content,
                        'created_at': str(message.created_at),
                        'number': count
                    }
                    json.dump(message_data, f, indent=4)
                    count += 1
                f.write("]")
                
        print(f"{ctx.message.channel}: Channel history refreshed and saved locally.")
    except Exception as e:
        print(f"Error occurred: {e}")