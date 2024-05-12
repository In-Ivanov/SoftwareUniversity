import re


def valid_function(dest_data):
    pattern = r"(\=|\/)([A-Z][A-Z-a-z]{2,})\1"
    valid_destination = []
    travel_points = 0
    result = re.finditer(pattern, dest_data)

    for curent_destination in result:
        valid_destination.append(curent_destination.group(2))
        travel_points += len(curent_destination.group(2))

    print(f"Destination: {', '.join(valid_destination)}\n"
          f"Travel points: {travel_points}")

date = input()
valid = valid_function(date)


