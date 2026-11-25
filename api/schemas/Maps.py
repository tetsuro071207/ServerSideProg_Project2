from pydantic import Field, BaseModel

class MapBase(BaseModel):
    MapName: str

class MapCreate(MapBase):
    """Body of a post request"""
