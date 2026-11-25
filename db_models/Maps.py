from sqlalchemy import Integer, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBMaps(Base):
    __tablename__ = "Maps"

    __table_args__ = ()

    MapID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    MapName: Mapped[str] = mapped_column(String)
