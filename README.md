# 🏢 Workplace Sensor Monitor

A REST API built with Python and FastAPI that monitors 
real-time room sensor data and sends automated alerts 
when temperature or occupancy thresholds are exceeded.

Built as a prototype of the kind of workplace IoT 
monitoring systems used in facilities management platforms.

---

## 🔧 Tech Stack

- Python / FastAPI
- Webhook integration (Discord)
- In-memory data store (swappable for MS SQL or Postgres)
- Environment variables for secure credential management

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rooms` | Get all rooms and sensor readings |
| GET | `/rooms/{room_id}` | Get a specific room |
| POST | `/rooms/{room_id}/sensor` | Push a new sensor reading |
| GET | `/simulate` | Simulate random sensor readings |

---

## ⚠️ Alert System

Alerts fire automatically via webhook when:
- Room temperature exceeds **80°F**
- Room occupancy reaches **90% of capacity**

Proactive thresholds — a