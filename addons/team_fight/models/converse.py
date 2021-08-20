from addons import reaction

team_fight_converse = reaction.Reaction()
def t(t):
    async def a(ctx):
        print(t)
        await ctx.send(t)
    return a
team_fight_converse.add_reaction_list('t1', t('team_fight1'), emoji='🧡')
team_fight_converse.add_reaction_list('t2', t('team_fight2'), emoji='💛')
team_fight_converse.add_reaction_list('t3', t('team_fight2'), emoji='💚')

