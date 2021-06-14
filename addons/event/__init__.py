from addons.event.models import event


def setup(bot):
    bot.add_cog(event.event(bot))
