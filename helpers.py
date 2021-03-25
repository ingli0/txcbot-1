import os
import io
import time
import discord
from discord.ext import commands
from datetime import datetime


async def mute_timer(self, ctx: commands.Context, member: discord.Member, minutes: float) -> None:
        """
        Timer until the specified time, to remove the `mute` role
        :param member: The member to add the `mute` role to
        :param minutes: The amount of minutes to mute the member for
        """
        