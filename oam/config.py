import os

SERVICE_NAME = os.getenv("SERVICE_NAME", "OAM")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "1.0.0")

BAC_HOST = os.getenv("BAC_HOST", "bac")
BAC_PORT = os.getenv("BAC_PORT", "5002")

PORT = int(os.getenv("PORT", 5001))

MEMORY_LIMIT = "512 MB"
CPU_LIMIT = "0.5 Core"