import logging
from turtle import textinput

from discord.ext import commands
from addons import model
from discord import ui,app_commands
import discord

_logger = logging.getLogger(__name__)

# 573893554577866777 窩們一起學牛叫：O
# <@&750720404213203079> @美美管理員
#
# 727170387091259393 功德無量
# 734391146910056478 @TEST
MY_GUILD = discord.Object(id=727170387091259393)  # replace with your guild id

class Select(ui.Select):
    def __init__(self, options):

        # placeholder: Will be shown when no option is chosen
        # custom_id: The id of the select menu
        # options: The dropdown options which can be chosen
        # max_values: Indicates that max. 2 options can be picked
        super().__init__(placeholder="Select", custom_id="test", options=options, max_values=2)

    # This function is called when the user has chosen an option
    async def callback(self, interaction: discord.Interaction):
        # With the interaction parameter, you can send a response message.
        # With self.values you get a list of the user's selected options.
        print(self.values)
        await interaction.response.send_message(f"Done!", ephemeral=True)

class ViewButton(ui.View):

    # label: The label of the button which is displayed
    # style: The background color of the button
    @ui.button(label="Role Menu", style=discord.ButtonStyle.blurple)
    async def role_menu_btn(self, interaction: discord.Interaction, button_obj: ui.Button):
        # This function is called when a user clicks on the button

        # get the roles
        # test1_role = interaction.guild.get_role(1007237710295081020)
        # test2_role = interaction.guild.get_role(1007237773230620728)

        # check if user has the role or not
        # df1 = True if test1_role in interaction.user.roles else False
        # df2 = True if test2_role in interaction.user.roles else False
        df1 = True 
        df2 = True 
        options = [
            discord.SelectOption(label="Test 1", value="Test 1", default=df1),
            discord.SelectOption(label="Test 2", value="Test 2", default=df2)
        ]

        # create ui.Select instance and add it to a new view
        select = Select(options=options)
        view_select = ui.View()
        view_select.add_item(select)

        # edit the message with the new view
        await interaction.response.edit_message(content="Choose an option", view=view_select)
        
class Questionnaire(ui.Modal, title='Questionnaire Response'):
    name = ui.TextInput(label='Name')
    answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)
            

class event(model.Cog_Extension):

    _name = 'event'

    """ @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(meme_channel)
        await channel.send(f'{member} join')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(meme_channel)
        await channel.send(f'{member} leave') """

    @commands.Cog.listener()
    async def on_ready(self):

        await super().on_ready()
        # _logger.debug('event on_ready')

    @commands.Cog.listener()
    async def on_message(self, msg):
        channel_id = msg.channel.id
        author_id = msg.author.id
        content = msg.content
        msg_id = msg.id
        attachments = msg.attachments
        # print('ch_id:', channel_id, 'msg_id:', msg_id, 'aut_id:', author_id, 'con:', content, 'attach:', attachments)
        # if attachments and msg.author != self.bot.user:
        #     file = attachments[0]
        #     file.filename = f"test_{file.filename}"
        #     spoiler = await file.to_file()
        #     await msg.channel.send(file=spoiler)
        """ if(msg.content == "check_channel_id"):
            print(f'Dc_msg: {msg.channel.id}')
        if msg.content == '<:MeMe:616147400792342538>' and msg.author != self.bot.user:
            await msg.channel.send('<:MeMe:616147400792342538>') """ 

    @commands.command()
    async def cleartest(self, ctx, number):
        channel_id = ctx.channel.id
        # print(channel_id)
        # channel = self.bot.get_channel(only_meme_speak_channel)
        # if channel_id == only_meme_speak_channel:
        mgs = []
        number = int(number)
        async for message in ctx.channel.history(limit=int(number)):
            mgs.append(message)
        for m in mgs:
            print(m.content)
        await ctx.channel.delete_messages(mgs)

    @commands.command()
    async def event_test(self, ctx):
        async with ctx.typing():
            # do expensive stuff here
            await ctx.send('done!')

    @commands.command()
    async def event_test2(self, ctx):
        await ctx.send('test!')

    @commands.command()
    async def get_all_cogs(self, ctx):
        await ctx.send(self.bot.cogs)

    @commands.command()
    async def get_members(self, ctx):
        # 573893554577866777 窩們一起學牛叫：O
        # <@&750720404213203079> @美美管理員
        #
        # 727170387091259393 功德無量
        # 734391146910056478 @TEST
        server = ctx.bot.get_guild(727170387091259393)
        print(server)
        print(ctx.guild)
        role = ctx.guild.get_role(734391146910056478)
        member_ids = [member for member in role.members]
        print(member_ids)
        # return member_ids

    @commands.command()
    async def get_info(self, ctx):
        print(await ctx.bot.application_info())
        print(ctx.bot.owner_id())

    @commands.command()
    async def get_msg_id(self, ctx, number):
        pass
        # channel_id = ctx.channel.id
        # channel = self.bot.get_channel(only_meme_speak_channel)
        # if channel_id == only_meme_speak_channel:
        #     mgs = []
        #     number = int(number)
        #     n = 1
        #     async for message in ctx.channel.history():
        #         print(message.created_at, message.id)
        #         n += 1
        #         if n > number:
        #             break
    
    @commands.command()
    async def button(self, ctx):
        await ctx.send(
            'test', view=ViewButton()
        )
    
    @commands.command()
    async def input(self, ctx):
        input = ui.TextInput(label='test')
        view_input = ui.View()
        view_input.add_item(input)
        
        await ctx.send(
            'test', view=view_input
        )

    @commands.hybrid_command()
    async def input2(self, ctx):
        await ctx.response.send_modal(Questionnaire())
        
    @app_commands.command(name="test4")
    async def test4(self, ctx):
        await ctx.send("This is a hybrid command!")
        
    @app_commands.command(name="command-1")
    async def my_command(self, interaction: discord.Interaction) -> None:
        """ /command-1 """
        await interaction.response.send_message("Hello from command 1!", ephemeral=True)
        
    @commands.hybrid_command(name="ping")
    async def ping_command(self, ctx: commands.Context) -> None:
        """
        This command is actually used as an app command AND a message command.
        This means it is invoked with `?ping` and `/ping` (once synced, of course).
        """

        await ctx.send("Hello!")
    
async def setup(bot):
    await bot.add_cog(event(bot))