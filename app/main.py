
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="ESP32 Server",
    description="Backend API for ESP32 devices.",
    version="0.1.0",
)

class TaskCreate(BaseModel):
    title: str
    done: bool = False

class LampChange(BaseModel):
    st1: int = Field(default=0, ge=0, le=255)
    st2: int = Field(default=0, ge=0, le=255)

@app.get("/")
def LoginUser():
    return

@app.get("/health")
def get_health():
    return {"ok": True}

@app.get("/changes")
def get_changes():
    return

@app.get("/settings")
def get_settings():
    return

@app.get("/photos")
def get_photos():
    return

@app.get("/weather")
def get_weather():
    return

@app.get("/calendar")
def get_calendar():
    return

@app.get("/clock_alarms")
def get_clock_alarms():
    return

@app.get("/messages")
def get_messages():
    return

