import hikari
import lightbulb
from hikari.permissions import Permissions

kick_plugin = lightbulb.Plugin("kick", "kick member ")
kick_plugin.add_checks(
    lightbulb.checks.has_guild_permissions(hikari.Permissions.KICK_MEMBERS),
    lightbulb.checks.bot_has_guild_permissions(hikari.Permissions.KICK_MEMBERS),
    lightbulb.guild_only,
)
KICK_PERMISSIONS = Permissions.KICK_MEMBERS


@kick_plugin.command()
@lightbulb.add_cooldown(3, 3, lightbulb.UserBucket)
@lightbulb.option(
    "reason",
    "the reason for kicking the member",
    str,
    required=False,
    modifier=lightbulb.commands.OptionModifier.CONSUME_REST,
)
@lightbulb.option("user", "the user you want to kick", hikari.User, required=True)
@lightbulb.app_command_permissions(KICK_PERMISSIONS, dm_enabled=False)
@lightbulb.command("kick", "kick a member", auto_defer=True, pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def kick(ctx: lightbulb.Context, user, reason):
    res = reason or f"'No Reason Provided.' By {ctx.author.username}"
    await ctx.respond(f"Kicking **{user}**")
    await ctx.bot.rest.kick_member(user=user, guild=ctx.get_guild(), reason=res)
    await ctx.edit_last_response(f"Succesfully kicked `{user}` for `{res}`!")


def load(bot):
    bot.add_plugin(kick_plugin)


def unload(bot):
    bot.remove_plugin(kick_plugin)
