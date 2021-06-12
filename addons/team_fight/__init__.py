from addons.team_fight.models import team_fight



def setup(bot):
    bot.add_cog(team_fight.team_fight(bot))