import discord
import time
import asyncio
from discord.ext import commands
from discord.utils import get
import random
import io
import os
import textblob
from gtts import gTTS
 
import helpers


from datetime import datetime
client = commands.Bot(command_prefix= '.')
client.remove_command('help')


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

                 'rota argotera.', 

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


@client.command(aliases=['fight', 'pali'])
async def _bet(ctx, omada1, *,omada2):
    apan =[omada1 ,
    omada2,
    'isopalia']
    await ctx.send(f'match: {omada1}-{omada2}\nto teliko apotelesma tou agona einai: {random.choice(apan)}') 

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
async def kolitos(ctx):
    await ctx.send(f' gia sou <@&822590182918193192> :blue_heart: ')


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
async def diss(ctx):
    await ctx.send(f'<@621247745474428941> https://www.youtube.com/watch?v=yGk1bjE5jAQ&ab_channel=articuno')

 


@client.command(aliases=['code', 'github'])
async def _github(ctx):
    await ctx.send(f'https://github.com/inbogia/txcbot')


@client.command()
async def dm(ctx):
    author = ctx.message.author 
    embed = discord.Embed(
        colour= discord.Colour.blurple()
    )
    
    embed.set_author(name ='den eisai asfalis')
    embed.add_field(name = 'na ksereis se parakoulouthaw', value='-',inline= False)

    await author.send(embed=embed)


@client.command(aliases=['toxic', 'toxicguy3'])
async def _toxic(ctx):
     
    await ctx.send(f' http://toxicguy3.ml/?i=1 enjoy')

@client.command()
async def rules(ctx):
    author = ctx.message.author 

    embed = discord.Embed(
        colour= discord.Colour.red()
    )
    embed.set_author(name ='Rules')
    embed.add_field(name = 'Rule #1', value='No spam ',inline= False)
    embed.add_field(name = 'Rule #2', value='Be respectful',inline= False)
    embed.add_field(name = 'SE PERIPTWSH PARABISASIS', value='se periptwsh parbiasis tha uparxoun oi analoge timories',inline= False)
    
    await ctx.send(embed=embed)

@client.command()
async def rule1(ctx):
    author = ctx.message.author 

    embed = discord.Embed(
        colour= discord.Colour.red()
    )
    embed.add_field(name = 'Rule #1', value='No spam ',inline= False)
    await ctx.send(embed=embed)

@client.command()
async def rule2(ctx):
    author = ctx.message.author 

    embed = discord.Embed(
        colour= discord.Colour.red()
    )
    embed.add_field(name = 'Rule #2', value='Be respectful',inline= False)
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    author = ctx.message.author 

    embed = discord.Embed(
        colour= discord.Colour.orange()
    )

    embed.set_author(name ='Help')
    embed.add_field(name = '8ball', value='kaneis mia erwtish kai sou epistrefw mia apantish',inline= False)
    embed.add_field(name = 'clr', value='diagrafw minimata',inline= False)
    embed.add_field(name = 'cs', value='tagarw ton mhtso gia na paiksei cs',inline= False)
    embed.add_field(name = 'diss', value='akou to kalitero diss olwn twn epoxwn',inline= False)
    embed.add_field(name = 'dm', value='sou stelnw dm',inline= False)
    embed.add_field(name = 'fight', value='dwse 2 onomata pou tha paiksoun ksilo kai tha sou pw to teliko apotelesma',inline= False)
    embed.add_field(name = 'github ', value='github link gia na deis pws me eftiaksan',inline= False)
    embed.add_field(name = 'help', value='deixnei auto to minima',inline= False)
    embed.add_field(name = 'kalimera ', value='se kalimerizw',inline= False)
    embed.add_field(name = 'mute', value='mute enan xristh epeidh den ekatse fronima',inline= False)
    embed.add_field(name = 'kalitos', value='kanw tag tous kolitous mou :blue_heart:',inline= False)
    embed.add_field(name = 'toxic', value='to kaliterw site olwn ton epoxwn',inline= False)
    embed.add_field(name = 'picon', value='sou dixnw tin eikona profile enos xristh',inline= False)
    embed.add_field(name = 'rules', value='kanones tou server pou prepei na akoulouthiseis',inline= False)
    embed.add_field(name = 'sm', value='bazw slowmode',inline= False)
    embed.add_field(name = 'unmute', value='kanw unmute kapion',inline= False)
    embed.add_field(name = 'tr', value='metafrazw kati sta ellinika',inline= False)

    #await author.send(embed=embed)
    await ctx.send(embed=embed)

@client.command(name="translate", aliases=["trans", "tr"], brief="Translate text from a language to greek")
async def translate(ctx: commands.Context, *, text: str) -> None:

    blob = textblob.TextBlob(text)
    translate_from = blob.detect_language()
    translate_to = "el"
    try:
        text = str(blob.translate(to=translate_to))
    except textblob.exceptions.NotTranslated:
        print("Text was in 'el'")

    if text:
        await ctx.send(f"{ctx.author.mention} Translation from {translate_from} to {translate_to}: ```{text} ```")
    else:
        await ctx.send(f"{ctx.author.mention}. Couldn't translate")
    
 
 

client.run('Nzk0NjgxNTYyMTYzMDUyNjA1.X--W4A.x6EERviO96yqnANFrwG2iq028sM')
