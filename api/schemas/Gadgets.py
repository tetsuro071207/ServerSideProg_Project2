from pydantic import Field, BaseModel

class GadgetBase(BaseModel):
    GadgetName: str
    GadgetDescription: str

class GadgetCreate(GadgetBase):
    """Body of a post request"""
