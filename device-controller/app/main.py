from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import *

BATTERY_LEVEL = 90
MAX_SPEED = 140
# Valid values for dashboard are red, green and blue. Anything else will trigger an error 
DASHBOARD_COLOR = 'ondrej'

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4001",
    "http://127.0.0.1:4001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def getSpeed(maxSpeed):
    #return 140
    return randint(0, maxSpeed)

@app.get("/battery-level")
def batteryLevel():
    return {"battery": BATTERY_LEVEL}

@app.get("/dashboard-color")
def color():
    return {"color": DASHBOARD_COLOR}

@app.get("/current-speed")
def speed():
    return {"speed": getSpeed(MAX_SPEED)}

