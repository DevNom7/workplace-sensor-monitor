from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from database import rooms
from webhook import send_alert
import random

app = FastAPI(title="Workplace Sensor Monitor")

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Thresholds
TEMP_THRESHOLD = 80.0
OCCUPANCY_THRESHOLD = 0.9  # 90% capacity

# --- Models ---
class SensorUpdate(BaseModel):
    temperature: float
    occupancy: int

# --- Routes ---
#GETs
@app.get("/")
def dashboard():
    return {"message": "Workplace Sensor Monitor Running"}

@app.get("/rooms")
def get_all_rooms():
    """GET all rooms and their sensor data"""
    return rooms

@app.get("/rooms/{room_id}")
def get_room(room_id: str):
    """GET a specific room by ID"""
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    return rooms[room_id]

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse("dashboard.html")

#POSTS

@app.post("/rooms/{room_id}/sensor")
def update_sensor(room_id: str, data: SensorUpdate):
    """POST new sensor reading for a room"""
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")

    room = rooms[room_id]
    room["temperature"] = data.temperature
    room["occupancy"] = data.occupancy

    # Check thresholds and alert
    if data.temperature > TEMP_THRESHOLD:
        room["status"] = "alert"
        send_alert(room["name"], "High Temperature", data.temperature)

    elif data.occupancy / room["capacity"] >= OCCUPANCY_THRESHOLD:
        room["status"] = "warning"
        send_alert(room["name"], "Near Capacity", data.occupancy)

    else:
        room["status"] = "ok"

    return {"message": "Sensor updated", "room": room}

@app.get("/simulate")
def simulate_sensors():
    """Simulate random sensor readings for all rooms"""
    for room_id, room in rooms.items():
        room["temperature"] = round(random.uniform(68, 95), 1)
        room["occupancy"] = random.randint(0, room["capacity"])

        if room["temperature"] > TEMP_THRESHOLD:
            room["status"] = "alert"
            send_alert(room["name"], "High Temperature", room["temperature"])
        elif room["occupancy"] / room["capacity"] >= OCCUPANCY_THRESHOLD:
            room["status"] = "warning"
            send_alert(room["name"], "Near Capacity", room["occupancy"])
        else:
            room["status"] = "ok"

    return rooms