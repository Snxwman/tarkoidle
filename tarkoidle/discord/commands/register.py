import arc
from arc import GatewayClient as ArcGatewayClient
from arc import GatewayContext as ArcGatewayContext
from arc import GatewayPlugin as ArcGatewayPlugin

from tarkoidle.discord.bot import TarkoIdleBot

plugin = ArcGatewayPlugin('register')
arc_client = TarkoIdleBot.arc_client


@plugin.include
@arc.slash_command('register', 'Register a TarkoIdle Player account.')
async def register(ctx: ArcGatewayContext) -> None: ...

@arc.loader
def load(client: ArcGatewayClient) -> None:
    _ = client.add_plugin(plugin)
