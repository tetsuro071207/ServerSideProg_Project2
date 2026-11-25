from fastapi import APIRouter, Depends, HTTPException
from api.database import get_db
from api.schemas.Operator import OperatorCreate
from db_models.Operators import DBOperator
from db_models.OperatorWeapons import DBOperatorWeapons
from db_models.OperatorUtilities import DBOperatorUtilities
from sqlalchemy.orm import Session

router = APIRouter(prefix="/operators", tags=["operators"])

@router.get("/", response_model=None)
def read_operators(skip: int = 0, limit: int = 50, db = Depends(get_db)):
    operators = db.query(DBOperator).offset(skip).limit(limit).all()
    return operators

@router.get("/{id}", response_model=None)
def read_one_operator(id: int, db = Depends(get_db)):
    operator = db.query(DBOperator).filter(DBOperator.OperatorID == id).first()
    if operator is None:
        raise HTTPException(status_code=404, detail="Operator Not found" )

    operator.IsDefender = not operator.IsAttacker

    return operator

@router.post("/", response_model=None)
def create_operator(create: OperatorCreate, db: Session = Depends(get_db)):
    operator = DBOperator(OperatorName=create.OperatorName, Health=create.Health, Speed=create.Speed, Difficulty=create.Difficulty, IsAttacker=create.IsAttacker)
    db.add(operator)
    db.commit()
    db.refresh(operator)
    return operator

@router.delete("/{id}", response_model=None)
def delete_operator(id: int, db: Session = Depends(get_db)):
    operator = db.query(DBOperator).filter(DBOperator.OperatorID == id).first()
    if operator is None:
        raise HTTPException(status_code=404, detail="Operator Not found" )

    db.delete(operator)
    db.commit()
    return "Operator deleted successfully"

@router.put("/{id}", response_model=None)
def update_operator(id: int, update: OperatorCreate, db: Session = Depends(get_db)):
    operator = db.query(DBOperator).filter(DBOperator.OperatorID == id).first()
    if operator is None:
        raise HTTPException(status_code=404, detail="Operator Not found" )

    operator.OperatorName = update.OperatorName
    operator.Health = update.Health
    operator.Speed = update.Speed
    operator.Difficulty = update.Difficulty
    operator.IsAttacker = update.IsAttacker

    db.commit()
    db.refresh(operator)
    return operator