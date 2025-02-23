from datetime import datetime
from platform import system
# The series order is ["f1", "f2", "f3", "fe", "f1-academy", "indycar", "motogp"]

segment_headings = ["FORMULA 1 - ROUND ", "FORMULA 2 - ROUND ", "FORMULA 3 - ROUND ",
                    "FORMULA E - ROUND ", "FORMULA 1 ACADEMY - ROUND ", "INDYCAR - ROUND ", "MOTOGP - ROUND "]
# The series who need their own heading
heading_series = ["f1", "fe", "indycar", "motogp"]

series_emote = [":red_square:", ":blue_square:", ":white_large_square:", ":yellow_square:",
                ":purple_square:", ":green_square:", ":black_large_square:"]

def output_race(series : str, selected_race : dict):
    heading, emote = determine_variables(series)
    output_string = ""

    #Event-Headline series present a headline for the whole event
    if series in heading_series:
        name = selected_race["name"]
        output_string += name
        if series == "f1":
            output_string += " Grand Prix"
        output_string += "\n"
        output_string.upper()

    round_num = selected_race["round"]
    output_string += heading + str(round_num) + "\n"

    sessions = selected_race["sessions"]
    for session_name, session_time in sessions.items():
        discord_name = convert_to_discord_name(session_name, emote, series)
        discord_time = convert_to_discord_timestamp(session_time)
        output_string += discord_name + discord_time + "\n"

    return output_string
def determine_variables(series : str):
    match series:
        case "f1":
            return segment_headings[0], series_emote[0]
        case "f2":
            return segment_headings[1], series_emote[1]
        case "f3":
            return segment_headings[2], series_emote[2]
        case "fe":
            return segment_headings[3], series_emote[3]
        case "f1-academy":
            return segment_headings[4], series_emote[4]
        case "indycar":
            return segment_headings[5], series_emote[5]
        case "motogp":
            return segment_headings[6], series_emote[6]
        case _:
            print ("Failure matching series! Please ensure that your series are spelled correctly")
            quit(-1)

def convert_to_discord_name(name : str, emote : str, series : str):
    session_name = name.upper()
    series_name = series.upper()
    discord_name = f"{emote} **{series_name} - {session_name}: **"
    return discord_name

# Adds necessary discord formatting for the timestamp
def convert_to_discord_timestamp(timestamp : str):
    unix_timestamp = str(convert_to_unix(timestamp))
    discord_timestamp = "<t:" + unix_timestamp + ":f>"
    return discord_timestamp

# Converts our timestring into a unix timestamp
def convert_to_unix(timestamp : str):
    date = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
    unix_timestamp = int(date.timestamp())
    return unix_timestamp