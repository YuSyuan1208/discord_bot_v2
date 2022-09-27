from addons.event.models import event


async def setup(bot):
    await bot.add_cog(event.event(bot))
