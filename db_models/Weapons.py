from sqlalchemy import Integer, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBWeapons(Base):
    __tablename__ = "Weapons"

    __table_args__ = ()

    WeaponID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    WeaponName: Mapped[str] = mapped_column(String)
    Damage: Mapped[int] = mapped_column(Integer, nullable=False)
    Magazine: Mapped[int] = mapped_column(Integer, nullable=False)
    MaxCapacity: Mapped[int] = mapped_column(Integer, nullable=False)
    WeaponType: Mapped[str] = mapped_column(String)