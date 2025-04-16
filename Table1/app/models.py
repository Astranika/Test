from sqlmodel import SQLModel, Field
from typing import  Optional
from datetime import datetime
from sqlalchemy import Column, String

class Table(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(100), nullable=False))
    seats: int
    location: str = Field(sa_column=Column(String(100), nullable=False))


class TableCreate(SQLModel):
    name: str
    seats: int
    location: str



class Reservation(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_name: str = Field(sa_column=Column(String(100), nullable=False))
    table_id: int
    reservation_time: datetime
    duration_minutes: int

class ReservationCreate(SQLModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int
