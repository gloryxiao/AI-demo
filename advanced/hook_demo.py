from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient, HookMatcher, HookContext
import asyncio
from typing import Any

# 定义钩子函数：检查并阻止危险Bash命令
async def block_dangerous_bash(
    input_data: dict[str, Any],
    tool_use_id: str | None,
    context: HookContext
) -> dict[str, Any]:
    tool_name = input_data.get('tool_name', '')
    if tool_name == "Bash":
        command = input_data['tool_input'].get('command', '')
        if 'rm -rf /' in command:
            print("[安全警告] 危险命令被阻止！")
            return {
                'hookSpecificOutput': {
                    'hookEventName': 'PreToolUse',
                    'permissionDecision': 'deny',
                    'permissionDecisionReason': '危险命令被阻止'
                }
            }
    return {}

async def hooks_example():
    options = ClaudeAgentOptions(
        allowed_tools=["Bash"],
        hooks={
            'PreToolUse': [
                HookMatcher(matcher='Bash', hooks=[block_dangerous_bash]) # 仅匹配Bash工具
            ]
        }
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query("使用 Bash 执行命令 rm -rf /tmp")
        async for message in client.receive_response():
            print(message)

if __name__ == "__main__":
    asyncio.run(hooks_example())