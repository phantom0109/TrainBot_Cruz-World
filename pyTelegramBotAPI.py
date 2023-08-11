from skpy import Skype
import base64
import traceback
 
username = "goldenshark0805@gmail.com"
message = "goldenshark1!"
message_bytes = message.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('utf-8')
password = base64_message
 
#  login 

try:
    # connect to Skype
    skype_connect = Skype(username, base64.b64decode(password.encode('utf-8')).decode('utf-8')) 
    chat = skype_connect.contacts["live:cid.2598fdf68306d97b"].chat
    filePath = "C:/1.jpg"
    name = "images.png"
    chat.sendFile(open(filePath, "rb"), name, image=True) # file upload
    print(chat.getMsgs())
except:
    print("An exception occurred")
    traceback.print_exc()