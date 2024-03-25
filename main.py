from pyrogram import Client
from config import *

app = Client(
	name="None",
	session_string=SESSION, 
	api_id=API_ID, 
	api_hash=API_HASH,
	device_model="ForwardScript",
	in_memory=True
	)

app.start()

if LIMIT == 0:LIMIT = None

messages = app.get_chat_history(
	FROM_ID, limit=LIMIT)

msg_list = [msg for msg in messages]
if REVERSED:
	msg_list = list(reversed(msg_list))

for message in msg_list:
	if hasattr(message, 'media') and message.media is not None:
		media_type = message.media.value
		media = getattr(message,media_type)
		if media_type=="web_page":continue
		file = app.download_media(message)
		media_handlers = {
		    "photo": app.send_photo,
		    "video": app.send_video
		}
		handler = media_handlers.get(media_type)
		if handler:
			handler(chat_id=TO_ID, **{media_type: file}, caption=message.caption)
	else:
		continue
		if message.text is not None:
			app.send_message(
				TO_ID,
				message.text
				)
		else:
			pass

app.stop()
