from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from .database import Base
from sqlalchemy import TIMESTAMP,text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ ="posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,default = True,server_default='TRUE',nullable=False)
    created_at  = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id  =Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    owner  = relationship("User")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,nullable=False,primary_key=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at  = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    date_of_birth =Column(TIMESTAMP(timezone=True),nullable=False)

class Votes(Base):
    __tablename__ ="votes"

    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)