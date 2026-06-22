import os

SERVICE_NAME = os.getenv("SERVICE_NAME", "BAC")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "1.0.0")

PORT = int(os.getenv("PORT", 5002))

MEMORY_LIMIT = "512 MB"
CPU_LIMIT = "0.5 Core"