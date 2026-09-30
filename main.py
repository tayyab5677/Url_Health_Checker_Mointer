import asyncio
import aiohttp
from App.checker import check_all_urls
from App.processor import (
    calculate_average_response_time,
    calculate_success_rate,
    get_down_urls,
    get_up_urls,
    result_generator,
)
from App.reports import create_report, save_report
from App.utils.file_utils import load_json
from App.validators import validate_urls


async def main():

    print("=" * 55)
    print("          URL HEALTH CHECKER & MONITOR")
    print("=" * 55)

    print("\nLoading URLs...")

    urls = load_json("data/urls.json")

    print(f"✓ {len(urls)} URLs loaded")

    print("\nValidating URLs...")

    try:
        validate_urls(urls)
        print(" All URLs are valid")

    except Exception as error:
        print(f" Validation Error: {error}")
        return

    print("\n" + "-" * 55)
    print("          ASYNC URL HEALTH CHECKING")
    print("-" * 55)

    print("\nStarting concurrent checks...\n")

    results = await check_all_urls(urls)

    for number, result in enumerate(
        result_generator(results),
        start=1,
    ):

        print(f"[{number}] {result.url}")

        print(f"    Status: {result.status}")

        print(
            f"    Status Code: "
            f"{result.status_code}"
        )

        print(
            f"    Response Time: "
            f"{result.response_time} ms"
        )

        if result.error:
            print(
                f"    Error: {result.error}"
            )

        print()

    up_urls = get_up_urls(results)
    down_urls = get_down_urls(results)

    success_rate = calculate_success_rate(results)

    average_time = calculate_average_response_time(
        results
    )

    print("-" * 55)
    print("                    SUMMARY")
    print("-" * 55)

    print(f"\nTotal URLs:       {len(results)}")
    print(f"URLs UP:          {len(up_urls)}")
    print(f"URLs DOWN:        {len(down_urls)}")
    print(f"Success Rate:     {success_rate}%")
    print(
        f"Average Response Time: "
        f"{average_time} ms"
    )

    report = create_report(results)

    save_report(
        report,
        "reports/health_report.json",
    )

    print("\n Report generated")
    print(
        " Saved to "
        "reports/health_report.json"
    )

    print("\n" + "=" * 55)
    print("          HEALTH CHECK COMPLETED")
    print("=" * 55)


if __name__ == "__main__":
    asyncio.run(main())