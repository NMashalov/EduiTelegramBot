from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from chat.db.models.base import Base
from chat.model.user import User


class User(Base):
    __tablename__ = "category"

    __pydantic_model__ = User

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    telegram_login: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
    surname: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
