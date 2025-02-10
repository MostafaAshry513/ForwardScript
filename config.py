import os

#The Chat ID You Want To Forward From
FROM_ID = int(os.getenv("FROM_ID", "The Chat ID You Want To Forward From"))

#The Chat ID You Want To Forward To
TO_ID = int(os.getenv("TO_ID", "The Chat ID You Want To Forward To"))

#Session String is a Quick Way To Login To Your Account From TG API
SESSION = os.getenv("SESSION", "Your Session String")

#Revers The Messages
REVERSED = os.getenv("REVERSED", "True").lower() == "true"

#The Message Number You Want To Start Forwarding From, 0 To Forwrad All The Chat Messages
START_MESSAGE = int(os.getenv("START_MESSAGE", "0"))

#The Messages Limit You Want To Forward, 0 To Forwrad All The Chat Messages
LIMIT = int(os.getenv("LIMIT", "Limit You Want"))

# You Can Get API ID And API HASH From: https://core.telegram.org/api/obtaining_api_id

API_ID = int(os.getenv("API_ID", "Your API ID")) #17058698

API_HASH = os.getenv("API_HASH", "Your API Hash") #088f8d5bf0b4b5c0536b039bb6bdf1d2
