minute = 0
seconds = 0
for i in range(0, 3):
    n = int(input())
    seconds += n
minute = seconds // 60
seconds = seconds % 60
if seconds < 10:
    print(f"{minute}:0{seconds}")
else:
    print(f"{minute}:{seconds}")

