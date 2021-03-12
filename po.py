import discord
from discord.ext import commands
from discord.utils import get
import random
import io
import youtube_dl
import os
from datetime import datetime
client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('tha katastrepw ton kosmo'))
    print('eimai sto grind')    

@client.command()
async def akous(ctx):
    await ctx.send(f'nai afentiko mou {round(client.latency*100)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['xwris amfibolia.', 

                 'nai.', 

                 'asto kalitera .', 

                 'pithanos.', 

                 ' oxi.', 

                 'den mporw na kserw.', 

                 'Yes.', 

                 'rota arhotera.', 

                 'kalitera min sou pw twra.', 

                 'den kserw.', 

                 'oi piges mou len oxi.', 

                 '100%.', 

                 'pithanon.',
                 
                 'isos',

                 'rwta ton roudi',

                 'den nomizw',

                 'den theleis na ksereis',

                 'aneta']
    await ctx.send(f'Erwtisi: {question}\nApantisi: {random.choice(responses)}')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clr(ctx,amount=5):
    if amount >26:
        await ctx.send(f'pola ebales')
    else:
         await ctx.channel.purge(limit=amount+1)



@client.command()
@commands.has_permissions( manage_channels=True)
async def sm(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"ebala slow mode {seconds} deuterolepta!")



@client.command()
async def kalimera(ctx):
    await ctx.send(f'kalimera aderfia')

@client.command()
async def cs(ctx):
    await ctx.send(f'<@288048756958691329> Μητσαρα παμε ενα cs')


@client.command()
async def panos(ctx):
    await ctx.send(f'<@607657777577590795> to tragoudi sou https://www.youtube.com/watch?v=obUHDyWFMi8')

@client.command(aliases=['bet', 'stoixima'])
async def _bet(ctx, omada1, *,omada2):
    apan =['aso',
    'diplo',
    'xi',
    'goal-goal',
    'over',
    'under']
    await ctx.send(f'match: {omada1}-{omada2}\nna to paiksis: {random.choice(apan)}') 

@client.command(name="picon", brief="Sends your icon's link")
async def get_icon(ctx: commands.Context, *, member: discord.Member = None) -> None:
    """
    Send the author's icon url to the channel
    :param member: (Optional) you can pass a member if you want to view this member's icon
    """

    if not member:
        url = ctx.author.avatar_url
        await ctx.send(f"{ctx.author.mention} your icon is located at: {url}")
    else:
        url = member.avatar_url
        await ctx.send(f"{ctx.author.mention}. This member's icon is located at: {url}")


@client.command()
async def xrr(ctx):
    await ctx.send(f'<@597538447837888512> xronia polla roudis na xairese to onama sou ')


@client.command()
async def kar(ctx):
    await ctx.send(f':heart: kai blasks ')

@client.command()
async def panoss(ctx):
    await ctx.send(f':no1 malakas ')

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

"""@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()"""


@client.command(
    name="mute", brief="Mute a member",
    description="Mute a member for the specified amount of minutes", aliases=["m", "voulwne"])
@commands.has_permissions( manage_channels=True)
async def mute(ctx: commands.Context, member: discord.Member, minutes: float = 5.0) -> None:
     
    muted_role = discord.utils.get(ctx.guild.roles,id=786702739345375232)
    await member.add_roles(muted_role)

    
    await ctx.send(f"{ctx.author.mention} muted {member.mention} for {minutes} minutes")
    
    synadelfos_role = ctx.guild.get_role(774337999307014174)
    await member.remove_roles(synadelfos_role)

@client.command(name="unmute", brief="Unmute a muted member")    
@commands.has_permissions( manage_channels=True)
async def unmute(ctx: commands.Context, member: discord.Member ):
    synadelfos_role = ctx.guild.get_role(774337999307014174)
    muted_role = discord.utils.get(ctx.guild.roles,id=786702739345375232)
    await member.add_roles(synadelfos_role)
    await member.remove_roles(muted_role)
    await ctx.send(f"{ctx.author.mention} unmuted {member.mention}" )

@client.command()
async def mlk(ctx):
    await ctx.send(f'<@607657777577590795> ksipna malaka')

@client.command()
async def diss(ctx):
    await ctx.send(f'<@621247745474428941> https://www.youtube.com/watch?v=yGk1bjE5jAQ&ab_channel=articuno')

client.run('Nzk0NjgxNTYyMTYzMDUyNjA1.X--W4A.Ord7g6zPxcmMUqaL8CUD2kRjxPc')
