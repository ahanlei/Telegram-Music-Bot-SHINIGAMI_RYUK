# used to get telegram session string code using either terminal or repl.it
"""Generate your Pyrogram Session String and send it to
Saved Messages of your Telegram account
requirements:
- Pyrogram
- TgCrypto
Get your Telegram API Key from:
https://my.telegram.org/apps
"""
import asyncio
import tgcrypto
from pyrogram import Client


async def main():
    api_id = int(input("API ID: "))
    api_hash = input("API HASH: ")
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            "**δΈβγοΈ» ππππππ£ππ£π₯π© οΈ»γβδΈ**:\nPyrogram Session String**:\n"
            f"`{await app.export_session_string()}`"
        )
        print(
            "δΈβγοΈ» ππππππ£ππ£π₯π© οΈ»γβδΈYour Pyrogram session string has been sent to "
            "Saved Messages of your Telegram account!"
        )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
