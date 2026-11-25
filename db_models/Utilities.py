from sqlalchemy import Integer, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBUtilities(Base):
    __tablename__ = "Utilities"

    __table_args__ = ()

    UtilityID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    UtilityName: Mapped[str] = mapped_column(String)
    UtilityDescription: Mapped[str] = mapped_column(String)
