from addons.team_fight.models import team_fight


async def setup(bot):
    await bot.add_cog(team_fight.team_fight(bot))
