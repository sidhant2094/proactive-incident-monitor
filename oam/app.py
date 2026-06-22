from flask import Flask, jsonify
from dotenv import load_dotenv
import logging
import requests
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
        "message": "OAM Service is Running",
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


@app.route("/call-bac")
def call_bac():

    logging.info("Calling BAC Service")

    try:

        url = f"http://{BAC_HOST}:{BAC_PORT}/status"

        response = requests.get(
            url,
            timeout=5
        )

        logging.info("BAC responded successfully")

        return jsonify({
            "caller": SERVICE_NAME,
            "status": "SUCCESS",
            "bac_response": response.json(),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        })

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "caller": SERVICE_NAME,
            "status": "FAILED",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT
    )