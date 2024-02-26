days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())


def plunder_gained(day, plunder, expect):
    gather = 0.0
    for g in range(1, day + 1):
        gather += daily_plunder
        if g % 3 == 0:
            gather += (daily_plunder * 0.5)
        elif g % 5 == 0:
            gather -= (gather * 0.3)
    return  gather


gain = plunder_gained(days, daily_plunder, expected_plunder)

if gain >= expected_plunder:
    print(f"Ahoy! {gain:.2f} plunder gained.")
else:

    print(f"Collected only {gain:.2f}% of the plunder.")
