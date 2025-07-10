from fastapi import FastAPI
from database.db import create_db_and_tables
from router.router import router  # <<<<<<
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",  
    "http://127.0.0.1:8080"
]

# Allow Vue frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(router)  # <<<<<< ใช้ Router จริง ๆ
