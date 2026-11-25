from pydantic import Field, BaseModel

class AttachmentBase(BaseModel):
    AttachmentName: str
    AttachmentType: str

class AttachmentCreate(AttachmentBase):
    """Body of a post request"""
