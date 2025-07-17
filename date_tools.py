from datetime import datetime

# Converts our timestring into a unix timestamp
def convert_to_unix(timestamp : str):
    date = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
    unix_timestamp = int(date.timestamp())
    return unix_timestamp