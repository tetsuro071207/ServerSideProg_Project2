from pydantic import Field, BaseModel

class WeaponBase(BaseModel):
    WeaponName: str
    Damage: int
    Magazine: int
    MaxCapacity: int
    WeaponType: str

class WeaponCreate(WeaponBase):
    """Body of a post request"""

