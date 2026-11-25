from sqlalchemy import Integer, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBGadgets(Base):
    __tablename__ = "Gadgets"

    __table_args__ = ()

    OperatorID: Mapped[int] = mapped_column(ForeignKey("Operators.OperatorID"), primary_key=True, autoincrement=True)
    GadgetName: Mapped[str] = mapped_column(String)
    GadgetDescription: Mapped[str] = mapped_column(String)
