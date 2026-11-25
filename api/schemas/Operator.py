from pydantic import Field, BaseModel

class OperatorBase(BaseModel):
    OperatorName: str
    Health: int 
    Speed: int 
    Difficulty: int
    IsAttacker: bool 

class OperatorCreate(OperatorBase):
    """Body of a post request"""
    # OperatorName: str
    # Health: int
    # Speed: int
    # Difficulty: int
    # IsAttacker: bool
