import os

CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 5))

SERVICES = [
    {
        "name": "OAM",
        "health_url": "http://oam:5001/health",
        "metrics_url": "http://oam:5001/metrics"
    },
    {
        "name": "BAC",
        "health_url": "http://bac:5002/health",
        "metrics_url": "http://bac:5002/metrics"
    }
]