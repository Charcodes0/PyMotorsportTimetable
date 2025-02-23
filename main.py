import json
import os

import data_downloader
from data_downloader import download_series, instantiate_directory
from race_printer import output_race

filepath = "\\_db\\"
year_path = '\\2025.json'

def request_series():
    series_options = ["f1", "f2", "f3", "fe", "f1-academy", "indycar", "motogp"]

    print("Welcome to the timetable system!")
    print("Please input the series you want from the following options:")
    print(series_options)

    print("Please enter in the format \"f1:n\" - where 'n' is the round number")
    races = input().lower().split(" ")
    interpret_series(races)

def interpret_series(series : list[str]):
    for r in series:
        round_details = r.split(":")
        round_num = int(round_details[1])
        process_series(round_details[0], round_num)

def process_series(series : str, num : int):
    download_series(series)
    directory = os.getcwd() + filepath + series + year_path
    with open(directory, "r") as json_file:
        data = json.load(json_file)

    # Searches through the data, finding the race with the corresponding round number
    selected_race = next((race for race in data['races'] if race['round'] == num), None)

    output_race(series, selected_race)

instantiate_directory()
request_series()