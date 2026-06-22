from flask import Flask, jsonify
from dotenv import load_dotenv
import logging
from datetime import datetime

load_dotenv()

from config import *
from state import *

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info(f"{SERVICE_NAME} Service Started")


@app.before_request
def before_request():
    increment_request_count()


@app.route("/")
def home():

    logging.info("Home endpoint called")

    return jsonify({
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "status": "running",
        "message": "BAC Service is Running",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/health")
def health():

    logging.info("Health endpoint called")

    return jsonify({
        "service": SERVICE_NAME,
        "status": "healthy",
        "version": SERVICE_VERSION,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/metrics")
def metrics():

    logging.info("Metrics endpoint called")

    return jsonify({
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "status": "healthy",
        "uptime_seconds": get_uptime(),
        "requests_served": get_request_count(),
        "memory_limit": MEMORY_LIMIT,
        "cpu_limit": CPU_LIMIT,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/status")
def status():

    logging.info("Status endpoint requested")

    return jsonify({
        "service": SERVICE_NAME,
        "status": "healthy",
        "version": SERVICE_VERSION,
        "message": "BAC is running successfully",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT
    )