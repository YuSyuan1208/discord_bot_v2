from addons.react.models import react


async def setup(bot):
    await bot.add_cog(react.react(bot))
