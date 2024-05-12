deposit_sum = float(input())
months = int(input())
year_percent = float(input())

interest = deposit_sum * (year_percent / 100)
month_interest = interest / 12
sum = deposit_sum + months * month_interest
print(sum)

