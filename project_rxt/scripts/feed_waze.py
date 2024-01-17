""" Web Scraping to Waze for cities Data Feed """

import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List

import requests

from scripts.waze.traffic_alert import (create_list_alert, get_list_alerts,
                                        insert_list_traffic_alert,
                                        update_list_alert)
from scripts.waze.traffic_jam import (create_list_jam, get_list_jams,
                                      insert_list_traffic_jam, update_list_jam)

URL_WAZE_FEED = "https://www.waze.com/row-partnerhub-api/partners/13191169720/waze-feeds/300d0e69-6c0b-4580-acaf-be25db2256ea?format=1&acotu=true&fa=true"
URL_VIEW_TRAFFIC_ALERTS = "http://localhost:8000/waze/v1/traffic-alerts/"
URL_VIEW_TRAFFIC_JAMS = "http://localhost:8000/waze/v1/traffic-jams/"
TIME_ZONE = 'America/Campo_Grande'
INTERVAL_SECONDS = 120  # Interval in seconds


def get_feed_waze() -> List[Dict[str, Any]]:
    """ Fetches the Waze feed and returns it as a list of dictionaries."""

    response: requests.models.Response

    try:
        response = requests.get(URL_WAZE_FEED, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request to {URL_WAZE_FEED} failed: {e}")
        return [{}]

    # Check if the response was successful
    if response.status_code == 200:
        # Create a dictionary to store the feed data
        print('Connected to Waze feed successfully.')
        data = response.json()
        return data
    else:
        # Return an empty list
        return [{}]


def process_traffic_alerts(data: List[Dict[str, Any]]) -> None:
    """ Processes a list of traffic alerts."""
    response_traffic_alerts_open = get_list_alerts(
            URL_VIEW_TRAFFIC_ALERTS,
            'True')
    print(f'Open traffic alerts qty: {len(response_traffic_alerts_open)}')

    # Creat list of traffic alerts
    traffic_alerts = create_list_alert(data, TIME_ZONE)
    print(f'Feed traffic alerts qty: {len(traffic_alerts)}')

    # Check if the response traffic alerts open
    if len(response_traffic_alerts_open) >= 0:

        # Update list of traffic alerts
        response_traffic_alerts_updates = update_list_alert(
            data,
            response_traffic_alerts_open,
            URL_VIEW_TRAFFIC_ALERTS)
        print('Number of finished traffic alerts:',
              len(response_traffic_alerts_updates['finished']))
        print('Number of updated date traffic alerts:',
              len(response_traffic_alerts_updates['update_date']))

    # Insert list of traffic alerts
    response_traffic_alerts = insert_list_traffic_alert(
        traffic_alerts, URL_VIEW_TRAFFIC_ALERTS)

    # Check number of traffic alerts created
    if len(response_traffic_alerts[0]) > 0:
        print(f'Number of new Traffic alerts: {len(response_traffic_alerts)}')
    else:
        print('There are no new traffic alerts.')

    return None


def process_traffic_jams(data: List[Dict[str, Any]]) -> None:
    """ Processes a list of traffic jams."""

    response_traffic_jams_open = get_list_jams(
        URL_VIEW_TRAFFIC_JAMS,
        'True')
    print(f'Open traffic jams qty: {len(response_traffic_jams_open)}')

    # Check if the response traffic jams open
    if len(response_traffic_jams_open) >= 0:
        # Update list of traffic jams
        response_traffic_jams_finished = update_list_jam(
            data,
            response_traffic_jams_open,
            URL_VIEW_TRAFFIC_JAMS)
        print('Finished traffic jams qty:',
              len(response_traffic_jams_finished))

    # Creat list of traffic jams
    response_traffic_jams = create_list_jam(data, TIME_ZONE)

    # Insert list of traffic jams
    response_traffic_jams = insert_list_traffic_jam(
        response_traffic_jams, URL_VIEW_TRAFFIC_JAMS)

    # Check number of traffic jams created
    if len(response_traffic_jams) > 0:
        print(f'Traffic jams qty: {len(response_traffic_jams)}')
    else:
        print('There are no new traffic jams.')

    return None


def fetch_feed(feed_url: str) -> None:
    """
    Fetches the feed from the given URL and saves it to a JSON file.
    Args:
        url (str): The URL of the feed.
    Returns:
        dict: The parsed JSON data.
    """
    data = get_feed_waze()
    # Check if the response was successful
    if len(data) > 0:
        print(f'Feed fetched successfully.')
    else:
        print('Feed fetched failed.')
        return None

    process_traffic_alerts(data)

    process_traffic_jams(data)

    return None


async def schedule_fetch(feed_url, interval) -> None:
    """
    Schedules the fetch_feed function to run every
    interval seconds.
    """
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        while True:
            await loop.run_in_executor(executor, fetch_feed, feed_url)
            print(f'Waiting {interval} seconds...')
            await asyncio.sleep(interval)


asyncio.run(schedule_fetch(URL_WAZE_FEED, INTERVAL_SECONDS))
