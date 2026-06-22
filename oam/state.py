import time

# Time when service started
START_TIME = time.time()

# Number of requests served
REQUEST_COUNT = 0


def increment_request_count():
    global REQUEST_COUNT
    REQUEST_COUNT += 1


def get_request_count():
    return REQUEST_COUNT


def get_uptime():
    return round(time.time() - START_TIME, 2)