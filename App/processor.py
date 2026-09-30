def result_generator(results):
    for result in results:
        yield result


def get_up_urls(results):
    return [result for result in results if result.status == "Up"]


def get_down_urls(results):
    return [result for result in results if result.status == "Down"]


def calculate_success_rate(results):
    if not results:
        return 0.0

    up_count = sum(result.status == "Up" for result in results)

    return round((up_count / len(results)) * 100, 2)


def calculate_average_response_time(results):
    successful_results = [
        result for result in results
        if result.status == "Up"
    ]

    if not successful_results:
        return 0.0

    total_time = sum(
        result.response_time
        for result in successful_results
    )

    return round(
        total_time / len(successful_results),
        2
    )