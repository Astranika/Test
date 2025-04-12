from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.models import Table, TableCreate
from app.dependencies import get_db

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/", response_model=list[Table])
def get_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()

@router.post("/", response_model=Table)
def create_table(table: TableCreate, db: Session = Depends(get_db)):
    db_table = Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.delete("/{table_id}")
def delete_table(table_id: int, db: Session = Depends(get_db)):
    table = db.get(Table, table_id)
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    db.delete(table)
    db.commit()
    return {"message": "Стол удалён"}