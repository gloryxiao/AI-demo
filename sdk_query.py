import asyncio
from claude_agent_sdk import ClaudeSDKClient
from claude_agent_sdk.types import AssistantMessage, TextBlock

async def continuous_conversation_example():
    async with ClaudeSDKClient() as client:
        # 第一次查询
        await client.query("告诉我法国的首都是哪里？")
        async for message in client.receive_response():
            print(message)
            # if isinstance(message, AssistantMessage):
            #     for block in message.content:
            #         if isinstance(block, TextBlock):
            #             print(block.text, end="")
            pass # 处理响应逻辑

        # 第二次查询，保留上下文
        await client.query("那个城市的人口是多少？")
        async for message in client.receive_response():
            print(message)
            pass # 处理响应逻辑

if __name__ == "__main__":
    asyncio.run(continuous_conversation_example())