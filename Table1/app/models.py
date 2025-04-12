from sqlmodel import SQLModel, Field
from typing import  Optional
from datetime import datetime

class Table(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    seats: int
    location: str

class TableCreate(SQLModel):
    name: str
    seats: int
    location: str


class Reservation(SQLModel,table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int


class ReservationCreate(SQLModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int