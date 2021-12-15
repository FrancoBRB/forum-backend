from pydantic import BaseModel
from typing import Optional, Text, List
from datetime import datetime
from . import user

class Comment(BaseModel):
    body: Text
    author: user.User
    published_date: datetime = datetime.now()

class Post(BaseModel):
    title: str
    body: Text
    author: user.User
    published_date: datetime = datetime.now()
    comments : List[Comment]