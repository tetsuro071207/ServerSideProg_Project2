from sqlalchemy import Integer, ForeignKey, String, CheckConstraint, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBOperator(Base):
    __tablename__ = "Operators"
    
    __table_args__ = (
        CheckConstraint("Health <= 3", name="MxOpHealth"),
        CheckConstraint("Speed <= 3", name="MxOpSpeed"),
        CheckConstraint("Difficulty <= 3", name="MxOpDifficulty"),
        CheckConstraint("Health >= 1", name="MnOpHealth"),
        CheckConstraint("Speed >= 1", name="MnOpSpeed"),
        CheckConstraint("Difficulty >= 1", name="MnOpSpeed"),
    )

    OperatorID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    OperatorName: Mapped[str] = mapped_column(String)
    Health: Mapped[int] = mapped_column(Integer, nullable=False)
    Speed: Mapped[int] = mapped_column(Integer, nullable=False)
    Difficulty: Mapped[int] = mapped_column(Integer, nullable=False)
    IsAttacker: Mapped[bool] = mapped_column(Boolean, nullable=False)
    