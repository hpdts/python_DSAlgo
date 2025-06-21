from typing import Union

from uuid import uuid4

from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# Using this example FastAPI app, model an API that would support a user chat experience powered by AI (think: ChatGPT)
"""
Interactive Chat 
POST to send the prompt
GET to get the response
LLM langchain
"""

# conversation 1..
# conversation 2...
# conversation n...


# conversation 1:
# user: x
# assistant: y1
# assistant: y2
# ...
# user: another question
# assistant: answer

# [type here]
# What SOLID principle means

"""
conversation_id: {1}.

create table Conversation
int id,
date creation_date

create table user
int id,
string name

create table conversation_user:
int conversation_id,
int user_id



"""


class Conversation:
    def __init__(self, uuid):
        self.uuid = uuid        
        self.messages = []


class Interaction:
    def __init__(self, prompt, message):        
        self.prompt = prompt
        self.message = message


@app.post("/conversation/")
def create_conversation(conversation):
    #getUUID and create a new conversation
    uuid = uuid4()
    conversation = Conversation(uuid)
    return {"conversation": conversation}

@app.post("/prompt/")
def pass_prompt(conversation_id, data):
   # data.prompt
    message = call_llm(data.prompt)
    return {"message": "message"}

@app.get("/conversation/{conversation_id}")
def get_conversation(conversation_id):
    conversation = get_conversation(conversation_id)
    return {"conversation": conversation}

#header bearer:token
@app.get("/conversation/")
def get_conversation(user_id):
    conversations = get_conversations(user_id)
    return {"conversations": conversations}