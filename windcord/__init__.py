from .windcord import Windcord

async def setup(bot):
	await bot.add_cog(Windcord(bot))
