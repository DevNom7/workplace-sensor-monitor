# 🏢 Workplace Sensor Monitor

A real-time workplace environment monitoring system 
built with Python and FastAPI. Tracks room temperature 
and occupancy, fires automated webhook alerts when 
thresholds are exceeded, and displays live data on 
a clean dashboard.

Built as a prototype of IoT monitoring systems used 
in enterprise facilities management platforms.

🌐 Portfolio: naimlindsay.com

---

## 🎥 Demo

| Dashboard | API Docs |
|-----------|----------|
| Live room cards with status | Auto-generated Swagger UI |
| Color-coded alerts | Interactive endpoint testing |
| Simulate sensor readings | Full request/response docs |

---

## 🔧 Tech Stack

- **Python / FastAPI** — REST API backend
- **HTML / CSS / JavaScript** — Live dashboard frontend
- **Discord Webhooks** — Real-time alert notifications
- **Pydantic** — Request validation and data modeling
- **python-dotenv** — Secure credential management

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rooms` | Get all rooms and sensor readings |
| GET | `/rooms/{room_id}` | Get a specific room by ID |
| POST | `/rooms/{room_id}/sensor` | Push a new sensor reading |
| GET | `/simulate` | Simulate random sensor readings |
| GET | `/dashboard` | Live monitoring dashboard |
| GET | `/docs` | Interactive API documentation |

---

## ⚠️ Alert System

Alerts fire automatically via Discord webhook when:
- 🌡 Room temperature exceeds **80°F**
- 👥 Room occupancy reaches **90% of capacity**

Proactive thresholds — alerts fire before a problem 
becomes critical, giving facilities teams time to act.

---

## 🏗 Architecture