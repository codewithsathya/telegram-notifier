import json
import os
import asyncio
from dotenv import load_dotenv

from telethon import TelegramClient
from telethon.tl.types import PeerChannel
from telethon.tl.functions.messages import (GetHistoryRequest)

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient("client", api_id, api_hash)

user_input_channel = input("enter entity(telegram URL or entity id):")


async def main():
    await client.start()
    me = await client.get_me()
    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel
    my_channel = PeerChannel(int(user_input_channel))
    all_messages = []
    history = await client(GetHistoryRequest(
        peer=my_channel,
        offset_id=0,
        offset_date=None,
        add_offset=0,
        limit=10,
        max_id=0,
        min_id=0,
        hash=0
    ))
    messages = history.messages
    for message in messages:
        all_messages.append(message.to_dict())
    print(all_messages)


with client:
    client.loop.run_until_complete(main())
