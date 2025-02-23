import json
import os

import data_downloader
from data_downloader import download_series, instantiate_directory
from race_printer import output_race

filepath = "\\_db\\"
year_path = '\\2025.json'

def interpret_series(series : str, manual : bool):
    # Ensure directories are correctly formatted
    instantiate_directory()

    series_list = series.lower().split(" ")

    formatted_series = []

    for r in series_list:
        round_details = r.split(":")
        round_num = int(round_details[1])
        single_series = process_series(round_details[0], round_num)
        formatted_series.append(single_series)

    # Only print if code is running manually from command line
    if manual:
        for i in formatted_series:
            print(i)
    else:
        return formatted_series

def process_series(series : str, num : int):

    # Downloads the requested series
    download_series(series)
    directory = os.getcwd() + filepath + series + year_path
    with open(directory, "r") as json_file:
        data = json.load(json_file)

    # Searches through the data, finding the race with the corresponding round number
    selected_race = next((race for race in data['races'] if race['round'] == num), None)

    return output_race(series, selected_race)