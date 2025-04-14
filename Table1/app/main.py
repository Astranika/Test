from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import tables, reservations
from .database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(tables.router)
app.include_router(reservations.router)





