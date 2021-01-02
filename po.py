import discord
from discord.ext import commands
import random

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
async def clr(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions( manage_channels=True)
async def sm(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"ebala slow mode {seconds} deuterolepta!")

class const:
    def __init__(self):
        
        self.MODERATOR_ID = 607694678363471926
        self.SYNADELFOS_ROLE_ID = 774337999307014174
        self.MUTED_ROLE_ID = 786702739345375232

@client.command(name="mute", brief="Mute a member", )
async def mute(ctx: commands.Context, member: discord.Member, minutes: float = 5.0) -> None:
    if minutes > 60:
        await ctx.send(f"{ctx.author.mention} you can't mute someone for more than 1 hour.")
        return
    
    muted_role = ctx.guild.get_role(const.MUTED_ROLE_ID)

    if muted_role in member.roles:
        await ctx.send(f"{member.mention} is already muted")
        return
    
    await member.add_roles(muted_role)
    await ctx.send(f"{ctx.author.mention} muted {member.mention} for {minutes} minutes")

    synadelfos_role = ctx.guild.get_role(const.SYNADELFOS_ROLE_ID)
    await member.remove_roles(synadelfos_role)


client.run('Nzk0NjgxNTYyMTYzMDUyNjA1.X--W4A.Ord7g6zPxcmMUqaL8CUD2kRjxPc')
