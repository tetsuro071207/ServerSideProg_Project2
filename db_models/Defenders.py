from sqlalchemy import Integer, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBDefenders(Base):
    __tablename__ = "Defenders"

    __table_args__ = ()

    DefenderID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    OperatorID: Mapped[str] = mapped_column(ForeignKey("Operators.OperatorID"), nullable=False)