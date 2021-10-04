import discord
import asyncio
import itertools
import datetime
import os
import random
import datetime
from discord import message
from discord import asset
from discord import file
from discord_components import component
from discord_components.client import DiscordComponents
from mcipc.rcon.je.enumerations import Color
import psutil
from discord.abc import GuildChannel, User
from discord.ext.commands import bot
from discord.ext.commands.converter import GuildConverter
from discord.ext.commands.core import has_permissions
from discord.ext.commands.errors import BotMissingPermissions
import youtube_dl
import re
import traceback
import DiscordUtils
import json
import requests
#=====================================================================================================
from discord.utils import *
from discord import Client
from discord.ext.commands import clean_content
from mcipc.query import Client
from mcipc.rcon.je import Biome, Client 
from mcipc.rcon.be import Client
from mcipc.rcon.ee import Client 
from io import BytesIO
from utils import enum
from covid19dh import covid19
from discord.ext import commands
from python_utils.import_ import import_global
from discord import user
from async_timeout import timeout
from collections import UserDict
from discord.client import Client
from youtube_dl import YoutubeDL
from discord.utils import get
from discord import FFmpegPCMAudio, PCMVolumeTransformer
from discord.utils import *
from setuptools import setup
from discord import FFmpegPCMAudio
from discord import utils
from discord import user
from discord import colour
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands
from discord.utils import get
from mcstatus import MinecraftServer
from discord import channel
from discord import player
from discord import member
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from setuptools import setup
from discord import utils
from discord import FFmpegPCMAudio
from PIL import Image
from io import BytesIO


DiscordComponents(bot)
intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix= ".")
client.remove_command("help")
music = DiscordUtils.Music()

@client.event
async def on_ready():
    print("został włączony")
    await client.change_presence(activity=discord.Game(name="Podstawowa komenda - pomoc"))

#komendy
#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                                POMOC                                   ║ #ZROBIĆ
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command(aliases=['pomoc'])
async def help(ctx):
    embed=discord.Embed(title="**Pomoc DragonBot™**", description="Cześć, jestem wielofunkcyjnym botem posiadającym rzeczy typu powitania, pozegnania, autorole (wiecej niz jedna) czy antyinvite. Jeśli nie wiesz jak czego używać możesz również napisać do Administratora.", color=0x2255ec)
    embed.set_thumbnail(url="https://bukkit.org/data/avatars/l/91241/91241907.jpg?1478800527")
    embed.add_field(name="🚨 Administratorskie", value="**clear**, **ban**, **kick**, **unban**, **tempban**, **mute**, **unmute**, **tempmute**", inline=False)
    embed.add_field(name="💸 Ekonomia", value="**zostanie dodana**", inline=True)
    embed.add_field(name="🎵 Muzyka", value="**join**, **leave**, **play**, **pause**, **resume**, **stop**, **loop**, **queue**, **np**, **skip**, **volume**, **remove**", inline=False)
    embed.add_field(name="😂 4Fun", value="**8ball**", inline=True)
    embed.add_field(name="✨ Praktyczne", value="**avatar**, **userinfo**, **covid**", inline=False)
    await ctx.send(embed=embed)
#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                               CLEAR                                    ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit):
    await ctx.message.delete()
    limit = int(limit)
    deleted = await ctx.channel.purge(limit=limit)
    embed = discord.Embed(title='Pomyślnie usunięto', description=f'Usunięto {len(deleted)} wiadomości na kanale #{ctx.channel}', color=0x4fff4d)
    await ctx.channel.send(embed=embed)

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                                BAN                                     ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="reason"):
    await member.ban(reason=reason)
    embed=discord.Embed(title="Użytkownik zbanowany", color=0xe12d2d)
    embed.add_field(name="Administrator: ", value=f"{ctx.author.name}", inline=False)
    embed.add_field(name="Uzytkownik:", value=f"{member.mention}", inline=True)
    embed.add_field(name="Powód:", value=f"{reason}", inline=False)
    await ctx.send(embed=embed)

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                               KICK                                     ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.kick(reason=reason)
    embed=discord.Embed(title="Użytkownik wyrzucony", color=0xe12d2d)
    embed.add_field(name="Administrator: ", value=f"{ctx.author.name}", inline=False)
    embed.add_field(name="Uzytkownik:", value=f"{member.mention}", inline=True)
    embed.add_field(name="Powód:", value=f"{reason}", inline=False)
    await ctx.send(embed=embed)

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                               UNBAN                                    ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command()
@commands.has_permissions(manage_messages=True)
async def unban(ctx, user: discord.User):
    await ctx.guild.unban(user)                       
    embed=discord.Embed(title="Użytkownik odbanowany", color=0x01f92a)
    embed.add_field(name="Administrator: ", value=f"{ctx.author.name}", inline=False)
    embed.add_field(name="Odbanowany:", value=f"{user.mention}", inline=True)
    await ctx.send(embed=embed)

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                             TEMPBAN                                    ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command()
@commands.has_permissions(manage_messages=True)
async def tempban(ctx, user:discord.User, duration: int):
    await ctx.guild.ban(user)
    await asyncio.sleep(duration)
    await ctx.guild.unban(user)

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                               MUTE                                     ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                              UNMUTE                                    ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" Zostałes odciszony na serwerze: {ctx.guild.name} Przez administratora {ctx.author.name} ")
   embed = discord.Embed(title="Użytkownik odciszony ", description=f" Użytkownik {user.mention} Został odciszony przez administratora {ctx.author.name}",colour=discord.Colour.light_green())
   await ctx.send(embed=embed)

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                            TEMPMUTE                                    ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command()
@commands.has_permissions(manage_messages=True)
async def tempmute(ctx, member: discord.Member, time=0, reason=None):
    if reason == None:
        reason = "no reason provided"
    
    if member.id == ctx.author.id:
        await ctx.send(f"{ctx.author.mention}, you can't mute yourself")

    role = discord.utils.get(ctx.guild.roles, name="Muted")

    if role in ctx.guild.roles:
        await member.add_roles(role)
        await ctx.send(f"Muted {member.mention}")
        await asyncio.sleep(time)
        await member.remove_roles(role)
    else:
        await ctx.send("No role named `Muted`!")

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                          AWATAR UŻYTKOWNIKA                            ║ #działa
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command()
async def avatar(ctx, member : discord.Member = None):

        if member is None:
            embed = discord.Embed(title="Poprawne użycie: ```.avatar [użytkownik]```", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        else:
            embed2 = discord.Embed(title=f"Awatar użytkownika {member}", colour=0x0000ff, timestamp=ctx.message.created_at)
            embed2.add_field(name="Animowany?", value=member.is_avatar_animated())
            embed2.set_image(url=member.avatar_url)
            await ctx.send(embed=embed2)

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                                8ball                                   ║ #ZROBIONE
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses =['Nie.',
                'A daj ty mi spokuj.',
                'Tak.',
                'Może.',
                'Możliwe',
                'Zdecydowanie nie']
    responce = random.choice(responses)
    embed=discord.Embed(title="8ball!", color=0x01f92a)
    embed.add_field(name="Pytanie: ", value=f"{question}", inline=False)
    embed.add_field(name="Odpowiedź:", value=f"{responce}", inline=True)
    await ctx.send(embed=embed)

#╔════════════════════════════════════════════════════════════════════════╗
#║                                                                        ║
#║                               MUZYKA                                   ║ #ZROBIONE
#║                                                                        ║
#╚════════════════════════════════════════════════════════════════════════╝
@client.command()
async def join(ctx):
    await ctx.author.voice.channel.connect() #Joins author's voice channel

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"Gram teraz {song.name}")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")

@client.command()
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"Paused {song.name}")

@client.command()
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"Resumed {song.name}")

@client.command()
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")

@client.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")

@client.command()
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")

@client.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)

@client.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

@client.command()
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"Changed volume for {song.name} to {volume*100}%")

@client.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")

#nowe============================================================================={percentage}

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if not member: 
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=0xffcb00, timestamp=ctx.message.created_at, title=f"Użytkownik {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Na zlecenie {ctx.author}")
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="Użytkownik:", value=member.display_name, inline=False)
    embed.add_field(name="Dyskryminator:", value=member.discriminator, inline=False)
    embed.add_field(name="Status:", value=str(member.status).title(), inline=False)
    embed.add_field(name="Stworzony profil:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name="Dołączył na serwer:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name="Role:", value="".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="Najwyższa rola:", value=member.top_role.mention, inline=False)
    embed.add_field(name="Bot:", value=member.bot, inline=False)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.command()
async def covid(ctx, *, countryName = None):

        if countryName is None:
            embed=discord.Embed(title="Poprawne użycie: ```+covid [country]```", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)


        else:
            url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
            stats = requests.get(url)
            json_stats = stats.json()
            country = json_stats["country"]
            totalCases = json_stats["cases"]
            todayCases = json_stats["todayCases"]
            totalDeaths = json_stats["deaths"]
            todayDeaths = json_stats["todayDeaths"]
            recovered = json_stats["recovered"]
            active = json_stats["active"]
            critical = json_stats["critical"]
            casesPerOneMillion = json_stats["casesPerOneMillion"]
            deathsPerOneMillion = json_stats["deathsPerOneMillion"]
            totalTests = json_stats["totalTests"]
            testsPerOneMillion = json_stats["testsPerOneMillion"]

            embed2 = discord.Embed(title=f"**COVID-19 STATYSTYKI**!", description="Ta informacja nie zawsze jest aktualna, dlatego może nie być dokładna!", colour=0x0000ff, timestamp=ctx.message.created_at)
            embed2.add_field(name="**Region:**", value=country, inline=True)
            embed2.add_field(name="**Spraw:**", value=totalCases, inline=True)
            embed2.add_field(name="**Dzisiaj spraw:**", value=todayCases, inline=True)
            embed2.add_field(name="**Zgony:**", value=totalDeaths, inline=True)
            embed2.add_field(name="**Dzisiaj Zgony:**", value=todayDeaths, inline=True)
            embed2.add_field(name="**Wyleczonych:**", value=recovered, inline=True)
            embed2.add_field(name="**Aktywnych:**", value=active, inline=True)
            embed2.add_field(name="**Krytycznych:**", value=critical, inline=True)
            embed2.add_field(name="**Spraw w milionach**", value=casesPerOneMillion, inline=True)
            embed2.add_field(name="**Zgony w milionach:**", value=deathsPerOneMillion, inline=True)
            embed2.add_field(name="**Testów:**", value=totalTests, inline=True)
            embed2.add_field(name="**Testy w milionach:**", value=testsPerOneMillion, inline=True)
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
            await ctx.send(embed=embed2)




client.run("ODk0MjA5MjMwMTI1NTQzNDU1.YVmrPg.t7yyMTf8DadZhRhix_PPCFgibFY")