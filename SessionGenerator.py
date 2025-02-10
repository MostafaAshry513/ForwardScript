import asyncio
from pyrogram import Client

app = Client(
	name="ForwardScript",
	api_id=17058698,
	api_hash="088f8d5bf0b4b5c0536b039bb6bdf1d2",
	device_model="ForwardScript",
	in_memory=True
)

async def export_session():
	await app.start()
	session_string = await app.export_session_string()
	print("Session string: ", session_string)
	await app.stop()

asyncio.run(export_session())
