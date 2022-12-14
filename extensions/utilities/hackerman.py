import lightbulb
from random import random
from math import floor
from utils.quotes import jargonConstructs, jargonWordPool
from utils.const import VERIFIED_ROLE_ID
hack_plugin = lightbulb.Plugin("hackerman", "HAAAAAAAAAAAAAAAX")


@hack_plugin.command()
@lightbulb.add_cooldown(3, 3, lightbulb.UserBucket)
@lightbulb.add_checks(lightbulb.has_roles(VERIFIED_ROLE_ID))
@lightbulb.command("hackerman", "l33t h4x000r!11", aliases=["hack"])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def hackerman(ctx: lightbulb.Context):
    h = []

    def j(b):
        c = jargonWordPool[b]
        e = floor(random() * len(c))
        f = c[e]
        while f in h:
            f = c[floor(random() * len(c))]
        h.append(f)
        return f

    rnd = floor(random() * len(jargonConstructs))
    construct = jargonConstructs[rnd]

    e = 0
    while e < len(jargonWordPool):
        f = "{" + str(e) + "}"
        while construct.find(f) > -1:
            construct = construct.replace(f, j(e), 1)
        e += 1
        construct = construct[0].upper() + construct[1:]

    await ctx.respond(f"**{construct}**")


def load(bot):
    bot.add_plugin(hack_plugin)


def unload(bot):
    bot.remove_plugin(hack_plugin)
