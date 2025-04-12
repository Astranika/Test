from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..models import Reservation, ReservationCreate
from ..dependencies import get_db
from app.models import Table
router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/", response_model=list[Reservation])
def get_reservations(db: Session = Depends(get_db)):
    return db.query(Reservation).all()

@router.post("/", response_model=Reservation)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    table = db.get(Table, reservation.table_id)
    if not table:
        raise HTTPException(status_code=404, detail="Вы не можете забронировать столик которого нет")

    reservation_end = reservation.reservation_time + timedelta(minutes=reservation.duration_minutes)
    existing_reservations = db.query(Reservation).where(Reservation.table_id == reservation.table_id).all()

    for existing in existing_reservations:
        existing_end = existing.reservation_time + timedelta(minutes=existing.duration_minutes)
        if (reservation.reservation_time < existing_end and
                reservation_end > existing.reservation_time):
            raise HTTPException(status_code=400, detail="Столик на это время уже забронирован")

    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.get(Reservation, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(reservation)
    db.commit()
    return {"message": "Бронирование отменено"}