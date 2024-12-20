# bot.py
import os
import discord
from dotenv import load_dotenv
from ai import ask

# 환경 변수를 .env 파일에서 로딩
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')


@client.event
async def on_message(message):
    # 다른 사용자로부터의 메시지만 응답 (봇 자신으로부터의 메시지는 무시)
    if message.author == client.user:
        return

    # OpenAI API가 대답
    messages = [{"role": "user", "content": message.content}]
    response = ask(messages)
    # 메세지 전송
    await message.channel.send(response)


# 봇 작동
client.run(DISCORD_TOKEN)