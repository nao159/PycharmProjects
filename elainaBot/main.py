import discord
from discord.ext import commands

from setupConfig import settings

bot = commands.Bot(command_prefix=settings['PREFIX'])


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}'
    )


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} на сервере с {member.joined_at.strftime("%Y, %b %d")}')


@bot.command()
async def greet(msg):
    await msg.send("greet")


bot.run(settings['TOKEN'])
