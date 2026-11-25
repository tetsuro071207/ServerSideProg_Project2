from sqlalchemy import Integer, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBOperatorWeapons(Base):
    __tablename__ = "OperatorWeapons"

    __table_args__ = ()

    OperatorID: Mapped[str] = mapped_column(ForeignKey("Operators.OperatorID"), primary_key=True, autoincrement=True, nullable=False)
    WeaponID: Mapped[int] = mapped_column(Integer, nullable=False)