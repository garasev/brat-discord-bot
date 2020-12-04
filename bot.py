from time import sleep
import os
import discord
from discord.ext import commands

from discord import *
from mutagen.mp3 import MP3

import config
import data
# RUN
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client))


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is not None and str(before.channel.id) == config.MAX_LAVROV_CHANNEL and after.channel is not None:
        voice = discord.utils.get(client.voice_clients, guild=client.get_guild(650427120408854539))
        if voice and voice.is_connected():
            await voice.move_to(after.channel)
        else:
            voice = await after.channel.connect()

        name = os.path.normpath(config.PATH + '//' + 'max.mp3')

        voice.play(discord.FFmpegPCMAudio(name))
        audio = MP3(name)
        voice.volume = 100
        voice.is_playing()

        audio = audio.info.length if audio.info.length < 50 else 50
        sleep(audio)

        if voice and voice.is_connected():
            await voice.disconnect()
    if before.channel is None and after.channel is not None:
        if member.id not in data.data.keys():
            return
        voice = discord.utils.get(client.voice_clients, guild=client.get_guild(650427120408854539))
        if voice and voice.is_connected():
            await voice.move_to(after.channel)
        else:
            voice = await after.channel.connect()

        name = os.path.normpath(config.PATH + '//' + data.data[member.id])

        voice.play(discord.FFmpegPCMAudio(name))
        audio = MP3(name)
        voice.volume = 100
        voice.is_playing()

        audio = audio.info.length if audio.info.length < 50 else 50
        sleep(audio)

        if voice and voice.is_connected():
            await voice.disconnect()


@client.command()
async def set_max(ctx):
    print(ctx.message.author.server_permissions)


@client.command()
async def songs(ctx):
    tmp = ''
    for song in config.songs:
        tmp += song + '\n'
    await ctx.send(tmp)


@client.command()
async def test(ctx, *, arg):
    await ctx.send(arg)


@client.command()
async def set_song(ctx, *mp3):
    if len(mp3) == 0:
        author = ctx.message.author.id
        data.drop_song(author)
        await ctx.send('Песня упала')
        return
    if mp3[0] not in config.songs:
        await ctx.send('Тьфу, такой песни нет')
        return
    author = ctx.message.author.id
    if data.set_song_per_id(author, mp3[0]):
        await ctx.send('Песня заменена')
    else:
        await ctx.send('Песня поставлена')


client.run(config.TOKEN)