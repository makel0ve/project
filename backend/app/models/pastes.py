from datetime import datetime

from sqlalchemy import func, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .models_config import Base


class Paste(Base):
    __tablename__ = "pastes"
    
    url: Mapped[str] = mapped_column(String, index=True, unique=True, nullable=True)
    text: Mapped[str] = mapped_column(String, index=True, nullable=True)
    hashid: Mapped[str] = mapped_column(String, index=True, unique=True)
    start_life: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), default=datetime.utcnow)
    end_life: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), default=datetime.utcnow)