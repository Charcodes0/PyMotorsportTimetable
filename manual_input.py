from series_requester import interpret_series

def request_series():
    series_options = ["f1", "f2", "f3", "fe", "f1-academy", "indycar", "motogp"]

    print("Welcome to the timetable system!")
    print("Please input the series you want from the following options:")
    print(series_options)

    print("Please enter in the format \"f1:n\" - where 'n' is the round number")
    races = input()
    interpret_series(races)

request_series()