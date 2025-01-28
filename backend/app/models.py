from sqlalchemy import Column, Integer, String, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    filename = Column(String)
    storage_url = Column(String)

class DocumentContent(Base):
    __tablename__ = "document_content"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    content = Column(Text)
    metadata = Column(JSON)
