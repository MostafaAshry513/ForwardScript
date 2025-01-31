from pyrogram import Client

app = Client(
  "my_account",
  api_id=17058698,
  api_hash="088f8d5bf0b4b5c0536b039bb6bdf1d2"
  )

async def export_session():
    async with app:
        session_string = await app.export_session_string()
        print("session string: ", session_string)

import asyncio
asyncio.run(export_session())
