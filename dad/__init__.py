from .dad import Noodledad

async def setup(bot):
	await bot.add_cog(Noodledad(bot))