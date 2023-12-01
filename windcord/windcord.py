import discord
from redbot.core import commands
from redbot.core.config import Config
import os
import asyncio
import logging
import random
from random import choice
import re



class Windcord(commands.Cog):
    """
    windonly links
    """
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=Windcord
        )
    
    @commands.command()
    async def leaderboard(self, ctx):
        """Wind Leaderboard"""
        await ctx.send("<https://docs.google.com/spreadsheets/d/1nNdo4sA790aLqFIXqzCeT89ry8dbqPUYA2VmOMxnnF8/edit?usp=sharing>")

    @commands.command()
    async def donation(self, ctx):
        """Wind Donation Form"""
        await ctx.send("<https://docs.google.com/forms/d/e/1FAIpQLSemwRPtwP6QthuZBSS-hmNKOoZvbA_kOr3cm1gaBQ6quc91DQ/viewform>")

    @commands.command()
    async def recurring(self, ctx):
        """Wind Recurring Push Leaderboard"""
        await ctx.send("<https://docs.google.com/spreadsheets/d/1GqKo38YyVu_he6hSz0SvEoifVorpHVPZZtf3ioJ1zp8/edit?usp=sharing>")

    @commands.command()
    async def vortex(self, ctx):
        """Wind Vortex Pinglists"""
        await ctx.send("<https://docs.google.com/spreadsheets/d/1WWPrEBApFOicrf5Gi_-P-ke93v7Mf0xLQ5dvUjygVFI/edit?usp=sharing>")

    @commands.command()
    async def dragonform(self, ctx):
        """Dragon Entry Form"""
        await ctx.send("<https://docs.google.com/forms/d/e/1FAIpQLSddR6FWG6GC7cNauzlLiiAxlY9g3SyyBb3PaLe1UC3Jefojrw/viewform?c=0&w=1>")
    
    @commands.command()
    async def payout(self, ctx):
        """Average Exalt Payout"""
        await ctx.send("https://cdn.discordapp.com/attachments/1177437614446481428/1177437815873744987/MON_EY.png")

    @commands.command()
    async def savedom(self, ctx):
        """10kt to Save Dom"""
        await ctx.send("https://cdn.discordapp.com/attachments/190584358925631488/728001199370141777/9360e14461db416ea85cee19976e35b2.png")

async def setup(bot):
	await bot.add_cog(Windcord(bot))
