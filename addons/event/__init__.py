from addons.event.models.event import event


def setup(bot):
    bot.add_cog(event(bot))
