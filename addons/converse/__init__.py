from addons.converse.models import converse

async def setup(bot):
    await bot.add_cog(converse.converse(bot))