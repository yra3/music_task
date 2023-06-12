from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapped_column, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Uuid,
    create_engine,
    ForeignKey,
)

from src.config import settings

engine = create_engine(settings.DATABASE_URL)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    token = Column(String)
    audios = relationship("Audio", back_populates="user")


class Audio(Base):
    __tablename__ = "audios"

    id = Column(Uuid, primary_key=True, index=True)
    name = Column(String)
    filepath = Column(String)
    user_id = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="audios")


SessionLocal = sessionmaker(autoflush=False, bind=engine)
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)
