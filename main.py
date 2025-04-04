
from astrbot.api.event import filter
from astrbot.api.star import Context, Star, register
from astrbot.core.platform import AstrMessageEvent
import astrbot.core.message.components as Comp
from .data_source import get_be_server_status, get_java_server_status


@register("astrbot_plugin_mcping", "Zhalslar", "获取 Minecraft JE/BE 服务器 Motd 图片信息", "1.0.0")
class MCPingPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("mcp",alias={"mcping","MCP"}, desc="获取 Minecraft JE/BE 服务器 Motd 图片信息")
    async def on_command(self, event: AstrMessageEvent, server_ip: str = None):
        status_img = (await get_java_server_status(server_ip) or
                      await get_be_server_status(server_ip))
        if status_img:
            yield event.chain_result([Comp.Image.fromBytes(status_img)])
        else:
            yield event.plain_result("查询失败")




