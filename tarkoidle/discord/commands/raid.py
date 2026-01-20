import asyncio
from random import randint

import arc
from arc import GatewayClient as ArcGatewayClient
from arc import GatewayContext as ArcGatewayContext
from arc import GatewayPlugin as ArcGatewayPlugin

from tarkoidle import GAME
from tarkoidle.discord.bot import TarkoIdleBot
from tarkoidle.utils.emoji import SPINNER

plugin = ArcGatewayPlugin('raid')
arc_client = TarkoIdleBot.arc_client

maps: dict[str, int] = {
    'Ground Zero': 60,
    'Streets of Tarkov': 50,
    'Interchange': 35,
    'Customs': 40,
    'Factory': 25,
    'The Lab': 15,
    'Woods': 38,
    'Shoreline': 32,
    'Lighthouse': 18,
}

map_names: list[str] = list(maps.keys())


@plugin.include
@arc.slash_command('raid', 'Queue into a raid.')
async def raid(
    ctx: ArcGatewayContext,
    raid_map: arc.Option[str, arc.StrParams('Select a map', choices=map_names)],
    raid_time: arc.Option[str, arc.StrParams('Select a time', choices=GAME.times)],
) -> None:
    at_user = f'<@{ctx.user.id}>'

    raid_msg = await ctx.respond(f'{at_user} is loading into a raid on {raid_map} at {raid_time}')
    await asyncio.sleep(3)

    raid_timer = randint(14, 28)  # noqa: S311
    raid_msg = await raid_msg.edit(f'{SPINNER} Raid ends in {raid_timer} seconds')
    enemy = ''
    fight_ticks = 0
    dead = False
    died_to = ''
    loot_value = 0
    scav_kills = 0
    pmc_kills = 0
    boss_kills = 0

    while raid_timer > 0 and not dead:
        if fight_ticks > 0:
            death_roll = randint(1, 100)
            if (
                (enemy == 'scav' and death_roll > 85)     # 15% death
                or (enemy == 'pmc' and death_roll > 87)   # 39% death
                or (enemy == 'boss' and death_roll > 88)  # 24% death
            ):
                dead = True
                died_to = enemy

            fight_ticks -= 1
            if fight_ticks == 0 and not dead:
                scav_kills += 1 if enemy == 'scav' else 0
                pmc_kills += 1 if enemy == 'pmc' else 0
                boss_kills += 1 if enemy == 'boss' else 0
                raid_msg = await raid_msg.edit(
                    (f'{SPINNER} Raid ends in {raid_timer} seconds\nCurrently: killed a {enemy}')
                )

            raid_timer -= 2
            await asyncio.sleep(2)
            continue

        action_roll = randint(1, 100)

        match action_roll:
            case int() if 1 <= action_roll <= 50:
                action = 'moving'
            case int() if 50 < action_roll <= 85:
                action = 'looting'
                found_value = randint(1000, 90000)
                loot_value += found_value
            case int() if 85 < action_roll <= 100:
                enemy_type = randint(1, 10)
                if enemy_type <= 7:
                    action = 'fighting scavs'
                    enemy = 'scav'
                    fight_ticks = 1
                elif enemy_type < 10:
                    action = 'fighting PMCs'
                    enemy = 'pmc'
                    fight_ticks = 3
                else:
                    action = 'fighting a boss'
                    enemy = 'boss'
                    fight_ticks = 2
            case _:
                action = 'begging nikita to not kick him in the balls'

        raid_msg = await raid_msg.edit(
            (f'{SPINNER} Raid ends in {raid_timer} seconds\nCurrently: {action}')
        )
        await asyncio.sleep(1)
        raid_timer -= 1
        raid_msg = await raid_msg.edit(
            (f'{SPINNER} Raid ends in {raid_timer} seconds\nCurrently: {action}')
        )
        await asyncio.sleep(1)
        raid_timer -= 1

    kills = ''
    kills += f'{scav_kills} scavs,' if scav_kills > 0 else ''
    kills += f'{pmc_kills} PMCs,' if pmc_kills > 0 else ''
    kills += f'{boss_kills} bosses' if boss_kills > 0 else ''
    kills = kills[:-1] if kills[-1] == ',' else kills

    if dead:
        kill_msg = ''
        if len(kills) > 0:
            kill_msg = f'after killing {kills}'

        _ = await raid_msg.edit(f'{at_user} was killed by a {died_to} on {raid_map} {kill_msg}')
    else:
        kill_msg = 'and killed no one'
        if len(kills) > 0:
            kill_msg = f'and killed {kills}'

        _ = await raid_msg.edit(
            f'{at_user} extracted from {raid_map} with ₽{loot_value:,} worth of loot {kill_msg}'
        )


@arc.loader
def load(client: ArcGatewayClient) -> None:
    _ = client.add_plugin(plugin)
