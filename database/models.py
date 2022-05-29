from database.database_logic import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    privileges = Column(String, nullable=False, server_default=text('user'))

class Promo(Base):
    __tablename__ = "promo"

    item_id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    cathegory = Column(String, nullable=False)
    title = Column(String, nullable=False)
    old_price = Column(String, nullable=True)
    new_price = Column(String, nullable=False)
    weight = Column(String, nullable=True)
    img = Column(String, nullable=False)
    link = Column(String, nullable=False)
    website = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    