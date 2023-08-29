import os
from venv import logger
import disnake
from disnake.ext import commands
from datetime import datetime
from disnake import utils

bot = commands.Bot(command_prefix=commands.when_mentioned, help_command=None, intents=disnake.Intents.all(), test_guilds=[1067554815690952835])
CENSORED_WORDS = ["nigga", "niga", "naga", "dick", "пошел нахуй", "пидр", "нага", "нига", "нигга", "пососи хуя", "mamy ebal", "маму ебал", "ты хуй", "блядь ты", "твоя мама сучка", "я ебал твою телку", "ты корова", "админы хуи", "стафф хуйня", "сервер хуйня", "овнер пидор", "овнер сын шлюхи", "69 с тобой", "пошла нахуй", "Россия топ", "россия топ", "слава россии", "Слава Росии"]

@bot.command()
@commands.is_owner()
async def load(ctx, extension): # .load eco
    bot.load_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, У вас недостаточно прав для выполнение данной команды!")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"
        ))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content.lower() == censored_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} такие слова запрещены!", delete_after=15)

@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=1067826580681916416)
    channel = utils.get(bot.get_all_channels(), id=1067556311069372457) 

    embed = disnake.Embed(
        title="New member",
        description=f"**{member.name}#{member.discriminator}** - US **The server will help** you **find a person** for **__join for join__**.\n" 
                    "・The **server has created** **convenient channels** for this.\n" "・**__Example work__** - **you go** to **server** with whom **__arranged__**, and **__he goes__** to **__your__** **server**.\n" 
                    "・** Successful ** development!",
        color=0xffffff
    )

    await member.add_roles(role)
    await channel.send(embed=embed)

@bot.command()
async def role(ctx, target: disnake.Member):
    author = target
    guild = bot.get_guild(1067554815690952835)
    role = guild.get_role(1067827586534744115)

    await author.add_roles(role)

@bot.event
async def on_ready():
    await bot.change_presence(
        status=disnake.Status.online,
        activity=disnake.Streaming(
            name="Hello newcomers to the server ( Взаимный Вход на Сервер | JOIN FOR JOIN )", url="https://www.twitch.tv/twitch"
        ),
    )

bot.run('MTExMDI3OTQ2NjU5MDE0MjUyNA.GUnFH4.KMe8I5Vb6Fs7c-sojEaqaLUkfaGwJ-1ihf-SGk')
