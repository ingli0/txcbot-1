import discord
from discord.ext import commands
import random
import io
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


@client.command(name="hmm", aliases=["hm", "swirl"], brief="Distorts your icon")
async def hmm(ctx: commands.Context, *, user: discord.User = None) -> None:
    """Take's a user's icon and creates a gif swiverling it"""

    # Create a bytes-like object to save the user's avatar on
    image_file = io.BytesIO()

    if user:
        await user.avatar_url.save(image_file)
    else:
        await ctx.author.avatar_url.save(image_file)

    image_file.seek(0)

    # Get the gif
    img = await client.helpers.edit_swirl(image_file)
    img.seek(0)

    file = discord.File(img, filename="icon.gif")
    await ctx.send(file=file)


client.run('Nzk0NjgxNTYyMTYzMDUyNjA1.X--W4A.Ord7g6zPxcmMUqaL8CUD2kRjxPc')
