from claude_agent_sdk import ClaudeAgentOptions, query
import asyncio

async def options_example():
    options = ClaudeAgentOptions(
        system_prompt="你是一名专业的 Python 开发者", # 定义智能体角色
        allowed_tools=["Read", "Write", "Bash"], # 允许使用的内置工具
        permission_mode='acceptEdits', # 自动接受文件编辑，加速自动化
        cwd="./" # 设置工作目录，方便文件操作
    )

    async for message in query(
        prompt="创建一个名为 'sort_demo.py' 的 Python 快排算法工具, 存放在 advanced目录下",
        options=options
    ):
        print(message)
        pass # 处理响应逻辑

if __name__ == "__main__":
    asyncio.run(options_example())