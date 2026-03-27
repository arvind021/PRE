from pyrogram import Client
import asyncio
import config

from ..logging import LOGGER

assistants = []
assistantids = []

ASS_NAMES = ["NandAss1", "NandAss2", "NandAss3", "NandAss4", "NandAss5"]
ASS_STRINGS = [
    config.STRING1, config.STRING2, config.STRING3,
    config.STRING4, config.STRING5
]


class Userbot(Client):
    def __init__(self):
        self.clients = [
            Client(
                name=ASS_NAMES[i],
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(ASS_STRINGS[i]),
                no_updates=True,
            )
            for i in range(5)
        ]

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        log_names = ["One", "Two", "Three", "Four", "Five"]

        for i, (string, client) in enumerate(zip(ASS_STRINGS, self.clients)):
            if not string:
                continue
            num = i + 1
            await client.start()
            assistants.append(num)
            try:
                await client.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant {num} failed to access log group. Add assistant as admin!"
                )
                exit()
            client.id = client.me.id
            client.name = client.me.mention
            client.username = client.me.username
            assistantids.append(client.id)
            LOGGER(__name__).info(f"Assistant {log_names[i]} Started as {client.name}")

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        for string, client in zip(ASS_STRINGS, self.clients):
            try:
                if string:
                    await client.stop()
            except:
                pass
