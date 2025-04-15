from fastapi import FastAPI, HTTPException
from typing import List
from datetime import datetime
from schemas import MessageCreate, Message

app = FastAPI(title="Simple Chat API")

# In-memory storage for messages
messages_db: List[Message] = []
message_id = 1

@app.post("/messages/", response_model=Message)
def send_message(msg: MessageCreate):
    global message_id
    message = Message(
        id=message_id,
        username=msg.username,
        content=msg.content,
        timestamp=datetime.utcnow()
    )
    messages_db.append(message)
    message_id += 1
    return message

@app.get("/messages/", response_model=List[Message])
def get_all_messages():
    return messages_db

@app.get("/messages/user/{username}", response_model=List[Message])
def get_user_messages(username: str):
    user_msgs = [msg for msg in messages_db if msg.username == username]
    if not user_msgs:
        raise HTTPException(status_code=404, detail="No messages found for user")
    return user_msgs
