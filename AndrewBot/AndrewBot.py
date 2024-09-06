from client import client
from config import BOT_TOKEN
from functions import *


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


client.add_command(echo)
client.add_command(history)
client.add_command(refresh_channel_cache)
client.add_command(gaming)
client.add_command(ping)
client.add_command(stop)
client.add_command(set_channel)
client.add_command(target)


if __name__ == '__main__':
    client.run(BOT_TOKEN)