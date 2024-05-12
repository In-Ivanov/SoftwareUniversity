hour = int(input())
minutes = int(input())

new_minute = minutes + 15
if new_minute >= 60:
    hour += 1
    if hour >= 24:
        hour -= 24
    minutes = new_minute - 60
    if minutes < 10:
        print(f"{hour}:0{minutes}")
    else:
        print(f"{hour}:{minutes}")

else:
    if new_minute < 10:
        print(f"{hour}:0{new_minute}")
    else:
        print(f"{hour}:{new_minute}")


