from sqlalchemy import Integer, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBAttackers(Base):
    __tablename__ = "Attackers"

    __table_args__ = ()

    AttackerID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    OperatorID: Mapped[str] = mapped_column(ForeignKey("Operators.OperatorID"), nullable=False)