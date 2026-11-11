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

class Settings(BaseModel):
    lamp1: int = Field(default=0, ge=0, le=255)
    lamp2: int = Field(default=0, ge=0, le=255)
    brightness: int = Field(ge=0,le=100)

class HealthResponse(BaseModel):
    ok: bool

messages = {
    "1": "Hello, this is a test message."
}



login_available = False
Test_token = "test_token"
test_login = "admin"
test_password = "password"
lamp1_state = 0
lamp2_state = 0
brightness_state = 0

@app.get("/")
def get_login():
    if token := Test_token:
        login_available = True
        return {"token": token}
    return {"error": "Invalid token"}

@app.post("/")
def post_login(login: str, password: str):
    if login == test_login and password == test_password:
        login_available = True
        return {"token": Test_token}
    return {"error": "Invalid login or password"}

@app.get("/health")
def get_health() -> HealthResponse:
    return HealthResponse(ok=True)

@app.get("/changes")
def get_changes():
    return 

@app.get("/settings")
def get_settings() -> Settings:
    return Settings(lamp1=lamp1_state, lamp2=lamp2_state, brightness=brightness_state)

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
def get_messages(user_token: str):
    if user_token != Test_token:
        return {"error": "Not authorized"}
    return messages

@app.get("/messages/{message_id}")
def get_message(message_id: str, user_token: str):
    if user_token != Test_token:
        return {"error": "Not authorized"}
    if message_id in messages:
        return {"id": message_id, "message": messages[message_id]}
    return {"error": "Message not found"}

@app.post("/messages")
def post_message(message: str):
    if login_available:
        new_id = str(max((int(message_id) for message_id in messages), default=0) + 1)
        if len(messages) >= 100:
            oldest_id = next(iter(messages))
            del messages[oldest_id]

        messages[new_id] = message
        return {"id": new_id, "message": message}
    return {"error": "Not authorized"}
