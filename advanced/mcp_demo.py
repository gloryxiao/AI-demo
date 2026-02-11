from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeAgentOptions, ClaudeSDKClient
from typing import Any
import asyncio

# 1. 定义自定义工具
@tool("get_time", "获取当前的系统时间", {})
async def get_time(args: dict[str, Any]) -> dict[str, Any]:
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "content": [{
            "type": "text",
            "text": f"sean-mcp:当前时间：{current_time}"
        }]
    }

# 2. 创建 SDK MCP 服务器
time_server = create_sdk_mcp_server(
    name="system_utilities",
    version="1.0.0",
    tools=[get_time]
)

async def custom_tool_session():
    # 3. 配置并使用
    options = ClaudeAgentOptions(
        mcp_servers={"utils": time_server},
        allowed_tools=["mcp__utils__get_time"] # 工具名称格式：mcp__<server_name>__<tool_name>
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query("现在是几点几分？")
        async for message in client.receive_response():
            print(message)

if __name__ == "__main__":
    asyncio.run(custom_tool_session())