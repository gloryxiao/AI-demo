import asyncio
from claude_agent_sdk import query, AssistantMessage, TextBlock

async def basic_query_example():
    async for message in query(prompt="你好，请问claude-agent-sdk是什么？"):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text, end="")
    print()

if __name__ == "__main__":
    asyncio.run(basic_query_example())