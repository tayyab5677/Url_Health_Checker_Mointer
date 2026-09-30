import json

from App.processor import (
    calculate_average_response_time,
    calculate_success_rate,
    get_down_urls,
    get_up_urls,
)


def create_report(results):

    up_urls = get_up_urls(results)
    down_urls = get_down_urls(results)

    report = {
        "total_urls": len(results),
        "up": len(up_urls),
        "down": len(down_urls),
        "success_rate": calculate_success_rate(results),
        "average_response_time": calculate_average_response_time(results),

        "results": [
            {
                "url": result.url,
                "status": result.status,
                "status_code": result.status_code,
                "response_time": result.response_time,
                "error": result.error,
            }
            for result in results
        ],
    }

    return report


def save_report(report, filename):

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)