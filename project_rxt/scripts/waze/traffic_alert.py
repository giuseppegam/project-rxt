""" Traffic alert module."""
import datetime
from typing import Any, Dict, List

import pytz
import requests


def get_list_alerts(urls_view: str, filter: str) -> List[Dict[str, Any]]:
    """Get list alerts."""
    response_alerts = requests.get(urls_view+f'?filter-open={filter}',
                                   timeout=10)
    data_alerts = response_alerts.json()

    return data_alerts


def update_be_finished(data_alerts,
                       response_traffic_alerts_open, uudi_data_alerts,
                       URL_VIEW_TRAFFIC_ALERTS) -> List[Dict[str, Any]]:
    """Update list alerts be finished."""

    # Filter alerts not in open
    alerts_be_finished = [
        alert for alert in response_traffic_alerts_open
        if alert['uuid'] not in uudi_data_alerts
    ]

    print("Number of Traffic Alerts to be finished:", len(alerts_be_finished))

    response_traffic_alerts_finished: requests.Response

    try:
        response_traffic_alerts_finished = requests.put(
            (URL_VIEW_TRAFFIC_ALERTS+'?finished-at-open=true'),
            json=alerts_be_finished, timeout=10)
        response_traffic_alerts_finished.raise_for_status()
    except requests.RequestException as e:
        print(f"Request to {URL_VIEW_TRAFFIC_ALERTS} failed: {e}")
        return [{}]

    return response_traffic_alerts_finished.json()


def update_date(data_alerts,
                response_traffic_alerts_open, uudi_data_alerts,
                URL_VIEW_TRAFFIC_ALERTS) -> List[Dict[str, Any]]:
    """Update a date of list alerts."""

    alerts_be_update = [
        alert for alert in response_traffic_alerts_open
        if alert['uuid'] in uudi_data_alerts
    ]

    print(f'Traffic alerts to be update date: {len(alerts_be_update)}')

    try:
        response_traffic_alerts_update = requests.put(
            (URL_VIEW_TRAFFIC_ALERTS+'?update-at-open=true'),
            json=alerts_be_update, timeout=10
        )
        response_traffic_alerts_update.raise_for_status()
    except requests.RequestException as e:
        print(f"Request to {URL_VIEW_TRAFFIC_ALERTS} failed: {e}")
        return [{}]

    return response_traffic_alerts_update.json()


def update_list_alert(data_alerts,
                      response_traffic_alerts_open,
                      URL_VIEW_TRAFFIC_ALERTS) -> Dict[str, Any]:

    """Update list alerts."""
    # Create an empty list to store traffic alerts
    data_alerts = data_alerts['alerts']

    # Extract uuid from data_alerts
    uudi_data_alerts = {alert['uuid'] for alert in data_alerts}

    # Update list alerts be finished
    response_traffic_alerts_finished = update_be_finished(
        data_alerts, response_traffic_alerts_open,
        uudi_data_alerts, URL_VIEW_TRAFFIC_ALERTS)

    # Update list alerts be update
    response_traffic_alerts_update = update_date(
        data_alerts, response_traffic_alerts_open,
        uudi_data_alerts, URL_VIEW_TRAFFIC_ALERTS)

    response_updates = {
        'finished': response_traffic_alerts_finished,
        'update_date': response_traffic_alerts_update
    }

    return response_updates


def create_list_alert(data, time_zone: str) -> List[Dict[str, Any]]:
    """Insert list alerts."""
    # Create an empty list to store traffic alerts
    traffic_alerts = []
    data_alerts = dict(data)

    # Iterate through the alerts list
    for alert in data_alerts['alerts']:
        # Convert pubMillis to datetime and make it aware

        # Define the date and time
        date_time = datetime.datetime.fromtimestamp(
            alert['pubMillis']/1000.0)

        # Define the timezone
        timezone = pytz.timezone(time_zone)

        # Change the date and time to the timezone
        pub_millis = date_time.astimezone(timezone)

        # Convert datetime object to string
        pub_millis_str = pub_millis.strftime('%Y-%m-%d %H:%M:%S')

        # Create a dictionary to store the traffic alert data
        post_data = {
            'pubMillis': pub_millis_str,
            'location': alert['location'],
            'uuid': alert['uuid'],
            'magvar': alert['magvar'],
            'type': alert['type'],
            'subtype': alert['subtype'],
            'city': alert['city'],
            'road_type': alert['roadType'],
            'report_rating': alert['reportRating'],
            'reliability': alert['reliability'],
            'confidence': alert['confidence'],
            'report_by_municipality_user': alert['reportByMunicipalityUser']
        }

        # Check if the alert has a street name
        if 'street' in alert:
            post_data['street'] = alert['street']
        else:
            post_data['street'] = ''

        # Check if the alert has a report description
        if 'reportDescription' in alert:
            post_data['report_description'] = alert['reportDescription']

        # Check if the alert has a jam uuid
        if 'jam_uuid' in alert:
            post_data['jam_uuid'] = alert['jamUuid']

        # Check if the alert has a number of thumbs up
        if 'nThumbsUp' in alert:
            post_data['n_thumbs_up'] = alert['nThumbsUp']

        # Add the post_data dictionary to the list
        traffic_alerts.append(post_data)

    return traffic_alerts


def insert_list_traffic_alert(
        traffic_alerts: List[Dict[str, Any]],
        urls_view: str) -> List[Dict[str, Any]]:
    """Insert list alerts."""

    response_traffic_alert: requests.Response

    try:
        response_traffic_alert = requests.post(
            urls_view, json=traffic_alerts, timeout=10)
        response_traffic_alert.raise_for_status()
    except requests.RequestException as e:
        print(f"Request to {urls_view} failed: {e}")
        return [{}]

    return response_traffic_alert.json()
