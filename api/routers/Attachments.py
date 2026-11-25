from fastapi import APIRouter, Depends, HTTPException
from api.database import get_db
from db_models.Attachments import DBAttachments
from api.schemas.Attachments import AttachmentCreate
from sqlalchemy.orm import Session

router = APIRouter(prefix="/attachments", tags=["attachments"])

@router.get("/")
def read_Attachments(skip: int = 0, limit: int = 50, db = Depends(get_db)):
    attachments = db.query(DBAttachments).offset(skip).limit(limit).all()
    return attachments

@router.get("/{id}")
def read_one_attachment(id: int, db = Depends(get_db)):
    attachment = db.query(DBAttachments).filter(DBAttachments.AttachmentID == id).first()
    if attachment is None:
        raise HTTPException(status_code=404, detail="Attachment Not found" )

    return attachment

@router.post("/", response_model=None)
def create_attachment(create: AttachmentCreate, db: Session = Depends(get_db)):
    attachment = DBAttachments(AttachmentName=create.AttachmentName, AttachmentType=create.AttachmentType)
    db.add(attachment)
    db.commit()
    db.refresh(attachment)
    return attachment

@router.delete("/{id}", response_model=None)
def delete_attachment(id: int, db: Session = Depends(get_db)):
    attachment = db.query(DBAttachments).filter(DBAttachments.AttachmentID == id).first()
    if attachment is None:
        raise HTTPException(status_code=404, detail="Attachment Not found" )

    db.delete(attachment)
    db.commit()
    return "Attachment deleted successfully"

@router.put("/{id}", response_model=None)
def update_attachment(id: int, update: AttachmentCreate, db: Session = Depends(get_db)):
    attachment = db.query(DBAttachments).filter(DBAttachments.AttachmentID == id).first()
    if attachment is None:
        raise HTTPException(status_code=404, detail="Attachment Not found" )

    attachment.AttachmentName = update.AttachmentName
    attachment.AttachmentType = update.AttachmentType

    db.commit()
    db.refresh(attachment)
    return attachment