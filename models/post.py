from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts_table'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    author = relationship("User", back_populates="Posts")
    user_id = Column(Integer, ForeignKey("users.id"))

class Comment(Base):
    __tablename__ = 'posts_comments'

