import asyncio
from pyrogram import Client
from config import *

async def main():
	global LIMIT, REVERSED, START_MESSAGE, FROM_ID, TO_ID 
	async with Client(
		name="None",
		session_string=SESSION, 
		api_id=API_ID, 
		api_hash=API_HASH,
		device_model="ForwardScript",
		in_memory=True
	) as app:

		if LIMIT == 0: LIMIT = None

		messages = app.get_chat_history(FROM_ID, limit=LIMIT)
		msg_list = [msg async for msg in messages]

		if REVERSED:
			msg_list = list(reversed(msg_list))

		if START_MESSAGE != "0":
			msg_list = [msg for msg in msg_list if msg.id >= int(START_MESSAGE)]

		print(len(msg_list))
		print(START_MESSAGE, type(START_MESSAGE))

		for message in msg_list:
			if hasattr(message, 'media') and message.media is not None:
				media_type = message.media.value
				media = getattr(message, media_type)
				if media_type == "web_page":
					continue
				file = await app.download_media(message)
				media_handlers = {
					"photo": app.send_photo,
					"video": app.send_video,
					"document": app.send_document
				}
				handler = media_handlers.get(media_type)
				if handler:
					await handler(chat_id=TO_ID, **{media_type: file}, caption=message.caption)
					print("message sent")
				else:
					print(media_type)
			else:
				if message.text is not None:
					await app.send_message(TO_ID, message.text)
					print("message sent")

asyncio.run(main())
