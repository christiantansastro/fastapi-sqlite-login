from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Depends, Form
from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = "sqlite:///./users.db"  # Use a file-based SQLite database

engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String, unique=True, index=True),
    Column("password", String),
)

Base = declarative_base()

# Bind the database models to the database engine
Base.metadata.create_all(bind=engine)

# Configure the databases package to use the database URL
database = Database(DATABASE_URL)

app = FastAPI()

async def get_database():
    async with database.transaction():
        yield database

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the appropriate origin for your HTML page
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: Database = Depends(get_database)):
    query = users.select().where(users.c.username == username)
    user = await db.fetch_one(query)

    if user and user['password'] == password:
        return {"status": "success", "message": "Login successful"}

    raise HTTPException(status_code=401, detail="Invalid credentials")
