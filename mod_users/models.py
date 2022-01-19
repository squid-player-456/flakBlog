from sqlalchemy import Column, Integer, String


class User:
    id = Column(Integer, primary_key=True)
    fullname = Column(String(128), nullable=False, unique=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False, unique=False)
    role = Column(Integer, nullable=False, default=0)
