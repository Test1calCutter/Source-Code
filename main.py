import nextcord
import random
import aiohttp
from nextcord.ext import commands

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("online")

class back(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @nextcord.ui.button(label="Back!", style=nextcord.ButtonStyle.red, emoji="<:back:1039916794091143188>")
    async def teste3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator and interaction.user != None:
            embed = nextcord.Embed(title="Administration")
            embed.add_field(name="<:ban:1009109288905605191> ban",
                            value="Ban a user.\n\n**Usage:**\n!ban [user] (reason)\n**Example:**\n!ban @bilo Squishing bugs!\n",
                            inline=True)
            embed.add_field(name="<:kick:1009110618806165615> kick",
                            value="Kick a user.\n\n**Usage:**\n!kick [user] (reason)\n**Example:**\n!kick @bilo Bullying bugs!\n",
                            inline=True)
            await interaction.send(embed=embed, ephemeral=True, view=back())
        else:
            embed = nextcord.Embed(title=f"You don't have the permissions for this!")
            await interaction.send(embed=embed, ephemeral=True)

class cats(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @nextcord.ui.button(label="Administration!", style=nextcord.ButtonStyle.red, emoji="<:warn:1009108633621102632>")
    async def teste3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator and interaction.user != None:
            embed = nextcord.Embed(title="Administration")
            embed.add_field(name="<:ban:1009109288905605191> ban",
                            value="Ban a user.\n\n**Usage:**\n!ban [user] (reason)\n**Example:**\n!ban @bilo Squishing bugs!\n",
                            inline=True)
            embed.add_field(name="<:kick:1009110618806165615> kick",
                            value="Kick a user.\n\n**Usage:**\n!kick [user] (reason)\n**Example:**\n!kick @bilo Bullying bugs!\n",
                            inline=True)
            await interaction.send(embed=embed, ephemeral=True, view=back())
        else:
            embed = nextcord.Embed(title=f"You don't have the permissions for this!")
            await interaction.send(embed=embed, ephemeral=True)


@bot.slash_command(name="help", description="Commands and about")
async def help(ctx: nextcord.Interaction):
    embed = nextcord.Embed(title="About", description="Click a button to choose the category!")
    await ctx.send(embed = embed, view=cats())

@bot.slash_command(name="ban", description="Ban a member")
async def ban(ctx: nextcord.Interaction, member: nextcord.Member = None, *, reason="No reason specified"):
    if member is None:
        embed=nextcord.Embed(title="Something isn't right...")
        embed.add_field(name="Example:", value="**/ban [member] (reason)**")
        embed.set_footer(text='"[]" Required. "()" Optional.')
        await ctx.send(embed=embed)

    embed=nextcord.Embed(title="User " + member.name + " banned for: __**" + reason + "**__")
    await ctx.send(embed=embed)

    embed=nextcord.Embed(title="You got banned from \"" + ctx.guild.name + "\" for: __**" + reason + "**__")
    await member.send(embed=embed)
    await member.ban(reason=reason)


@bot.slash_command(name="kick", description="Kick a member")
async def kick(ctx: nextcord.Interaction, member: nextcord.Member = None, *, reason="No reason specified"):
    if member is None:
        embed=nextcord.Embed(title="Something isn't right...")
        embed.add_field(name="Example:", value="**/kick [member] (reason)**")
        embed.set_footer(text='"[]" Required. "()" Optional.')
        await ctx.send(embed=embed)

    embed=nextcord.Embed(title="User " + member.name + "kicked for: __**" + reason + "**__")
    await ctx.send(embed=embed)

    embed=nextcord.Embed(title="You got banned from \"" + ctx.guild.name + "\" for: __**" + reason + "**__")
    await member.send(embed=embed)
    await member.kick(reason=reason)


@bot.slash_command(name="meme", description="Get a random Meme")
async def meme(ctx: nextcord.Interaction):
    embed = nextcord.Embed(title="Here's a meme for you.", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)






bot.run("MTAzOTU1Mzk2NjE4ODUzNTgzOQ.GOsLwu.e9tClguPiDIvZEO9dsbpT9SEgPEv1wgvWERLmo")