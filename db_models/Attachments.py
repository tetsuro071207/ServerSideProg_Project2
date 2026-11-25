from sqlalchemy import Integer, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from db_models.base import Base

class DBAttachments(Base):
    __tablename__ = "Attachments"

    __table_args__ = ()

    AttachmentID: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    AttachmentName: Mapped[str] = mapped_column(String)
    AttachmentType: Mapped[str] = mapped_column(String)