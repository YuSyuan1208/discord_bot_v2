from addons.converse.models import converse

def setup(bot):
    bot.add_cog(converse.converse(bot))