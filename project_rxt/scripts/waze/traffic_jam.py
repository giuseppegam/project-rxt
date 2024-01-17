import datetime
from typing import Any, Dict, List

import pytz
import requests


def get_list_jams(urls_view: str, filter: str) -> List[Dict[str, Any]]:
    """Get list jams."""
    response_jams = requests.get(
        urls_view+f'?filter-open={filter}', timeout=10)
    data_jams = response_jams.json()

    return data_jams


def update_list_jam(data_jams,
                    response_traffic_jams_open,
                    URL_VIEW_TRAFFIC_JAMS):

    """Update list jams."""
    # Create an empty list to store traffic jams
    data_jams = data_jams['jams']
    print(f'Feed traffic jams qty: {len(data_jams)}')
    print(f'Open traffic jams qty: {len(response_traffic_jams_open)}')

    # Extract uuid from data_jams
    uudi_data_jams = {jam['uuid'] for jam in data_jams}

    # Filter jams not in open
    jams_be_finished = [
        jam for jam in response_traffic_jams_open
        if jam['uuid'] not in uudi_data_jams
    ]

    print(f'Traffic jams be finished qty: {len(jams_be_finished)}')

    response_traffic_jams_finished = requests.put(
        (URL_VIEW_TRAFFIC_JAMS+'?finished-at-open=true'),
        json=jams_be_finished, timeout=10
    )

    if response_traffic_jams_finished.status_code == 201:
        print('Traffic jam finished successfully.')

    jams_be_update = [
        jam for jam in response_traffic_jams_open
        if jam['uuid'] in uudi_data_jams
    ]

    print(f'Traffic jams be update qty: {len(jams_be_update)}')

    response_traffic_jams_update = requests.put(
        (URL_VIEW_TRAFFIC_JAMS+'?update-at-open=true'),
        json=jams_be_update, timeout=10
    )

    if response_traffic_jams_update.status_code == 201:
        print('Traffic jam updated successfully.')

    return response_traffic_jams_finished.json()


def create_list_jam(data, time_zone: str) -> List[Dict[str, Any]]:
    """Insert list jams."""
    traffic_jams = []
    data_jams = dict(data)

    # Iterate through the jams list
    for jam in data_jams['jams']:

        # Create a dictionary to store the traffic jam data
        post_data = {
            'uuid': jam['uuid'],
            'pubMillis': jam['pubMillis'],
            'line': jam['line'],
            'speed': jam['speed'],
            'speedKPH': jam['speedKMH'],
            'length': jam['length'],
            'delay': jam['delay'],
            'city': jam['city'],
            'road_type': jam['roadType'],
            'level': jam['level'],
            'turn_type': jam['turnType'],
        }

        # Convert pubMillis to datetime and make it aware

        # Define the date and time
        date_time = datetime.datetime.fromtimestamp(
            jam['pubMillis']/1000.0)

        # Define the timezone
        timezone = pytz.timezone(time_zone)

        # Change the date and time to the timezone
        pub_millis = date_time.astimezone(timezone)

        # Convert datetime object to string
        pub_millis_str = pub_millis.strftime('%Y-%m-%d %H:%M:%S')
        post_data['pubMillis'] = pub_millis_str

        # Check if the jam has a end_none
        if 'endNode' in jam:
            post_data['end_node'] = jam['endNode']

        # Check if the jam has a blocking alert uuid
        if 'blockingAlertUuid' in jam:
            post_data['blocking_alert_uuid'] = jam['blockingAlertUuid']

        # Check if the jam has a stardNode
        if 'startNode' in jam:
            post_data['start_node'] = jam['startNode']

        # Check if the jam has a lines
        if 'line' in jam:
            post_data['line'] = jam['line']

        # Check if the jam has a street name
        if 'street' in jam:
            post_data['street'] = jam['street']

        # Check if the jam has a segments
        if 'segments' in jam:
            post_data['segment'] = jam['segments']

        # Add the post_data dictionary to the list
        traffic_jams.append(post_data)

    return traffic_jams


def insert_list_traffic_jam(
        traffic_jams: List[Dict[str, Any]],
        urls_view: str) -> List[Dict[str, Any]]:

    """Insert list traffic jam."""
    response_traffic_jams = requests.post(
         urls_view, json=traffic_jams, timeout=10)

    if response_traffic_jams.status_code == 201:
        print('Traffic jam inserted successfully.')
    else:
        print('Failed to insert traffic jam.')

    return response_traffic_jams.json()
