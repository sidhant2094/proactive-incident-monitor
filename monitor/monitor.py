import requests
from datetime import datetime


def check_service(service):

    result = {
        "name": service["name"],
        "health": "DOWN",
        "metrics": None,
        "error": None
    }

    try:

        health = requests.get(
            service["health_url"],
            timeout=3
        )

        metrics = requests.get(
            service["metrics_url"],
            timeout=3
        )

        result["health"] = health.json()
        result["metrics"] = metrics.json()

    except Exception as e:

        result["error"] = str(e)

    return result


def print_report(results):

    print("\n" + "=" * 60)

    print(
        f"Monitoring Report : {datetime.now()}"
    )

    print("=" * 60)

    for service in results:

        print()

        print(f"Service : {service['name']}")

        if service["error"]:

            print("Status  : DOWN")
            print(f"Reason  : {service['error']}")

        else:

            print("Status  : HEALTHY")

            print(
                f"Uptime  : {service['metrics']['uptime_seconds']} sec"
            )

            print(
                f"Requests: {service['metrics']['requests_served']}"
            )

    print("=" * 60)