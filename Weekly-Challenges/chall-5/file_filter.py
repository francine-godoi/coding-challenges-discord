from discord.ext import commands

def setup(bot):
    bot.add_cog(FileFilter(bot=bot))

class FileFilter(commands.Cog):
    """Adds functionality to filter out sertant files based on their extention"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.accepted_extentions: List[str] = []

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        ... # Add your code here.