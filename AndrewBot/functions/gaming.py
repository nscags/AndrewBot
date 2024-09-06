'''
gaming.py
'''

from discord.ext import commands
import random

from client import client


# Function to check if guess is of correct type
def check(m):
    if m.content == 'stop': return True
    try: 
        int(m.content)
        return True
    except: 
        return False


@commands.command()
async def gaming(ctx, max_value=200):
    '''
    Number guessing game.
    Credit: Raymond Bard
    '''

    player_id = ctx.message.author.id
    answer = random.randint(0 , max_value)
    guess = -1
    tries = 0

    await ctx.send(f"<@{str(player_id)}> Guess a number between 0 and {max_value}!")

    while guess != answer:
        # wait for user to make a guess
        msg = await client.wait_for("message", check=check)

        # Only player gets to guess
        if msg.author.id == player_id:
            if msg.content == 'stop':
                await ctx.reply("Game Over.")
                break
            # if valid check guess vs answer
            guess = int(msg.content)
            if guess < 0 or guess > max_value:
                await ctx.reply(f"Your guess must be in the range of 0 and {max_value}")
            elif guess < answer: 
                await ctx.reply("The real answer is higher.")
                tries += 1
            elif guess > answer: 
                await ctx.reply("The real answer is lower.")
                tries += 1

    # Player found correct answer
    if msg.author.id == player_id and guess == answer:
        await ctx.reply(f"Congratulations <@{msg.author.id}>! You are correct, it took you " + str(tries) + " guesses")