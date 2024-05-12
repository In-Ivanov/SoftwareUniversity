stops = input()

while True:
    stop = input()
    if stop == "Travel":
        break
    fly = stop.split(":")
    action = fly[0]
    if fly[0] == "Add Stop":
        index = int(fly[1])
        string = fly[2]
        stops = stops[:index] + string + stops[index:]
        print(stops)

    if fly[0] == "Remove Stop":
        start_index = int(fly[1])
        end_index = int(fly[2]) + 1
        remove_string = stops[start_index:end_index]
        stops = stops.replace(remove_string, "")
        print(stops)

    if fly[0] == "Switch":
        old_string = fly[1]
        new_string = fly[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
            print(stops)
        else:
            print(stops)
print(f"Ready for world tour! Planned stops: {stops}")

