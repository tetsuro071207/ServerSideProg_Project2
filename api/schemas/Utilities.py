from pydantic import Field, BaseModel

class UtilityBase(BaseModel):
    UtilityName: str
    UtilityDescription: str

class UtilityCreate(UtilityBase):
    """Body of a post request"""
