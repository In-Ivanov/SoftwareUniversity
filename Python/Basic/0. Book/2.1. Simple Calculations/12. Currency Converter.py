num = float(input())
valute_one = input()
valute_two = input()

bgn_bgn = 1
bgn_usd = 1 / 1.79549
bgn_eur = 1 / 1.95583
bgn_gbp = 1 / 2.53405

usd_usd = 1
usd_bgn = 1.79549
usd_eur = 1.79549 / 1.95583
usd_gbp = 1.79549 / 2.53405

eur_eur = 1
eur_bgn = 1.95583
eur_usd = 1.95583 / 1.79549
eur_gbp = 1.95583 / 2.53405

gbp_gbp = 1
gbp_bgn = 2.53405
gbp_usd = 2.53405 / 1.79549
gbp_eur = 2.53405 / 1.95583

if valute_one == "BGN":
    if valute_two == "BGN":
        print(f"{num * bgn_bgn:.2f}", "BGN")
    elif valute_two == "USD":
        print(f"{num * bgn_usd:.2f}", "USD")
    elif valute_two == "EUR":
        print(f"{num * bgn_eur:.2f}", "EUR")
    elif valute_two == "GBP":
        print(f"{num * bgn_gbp:.2f}", "GBP")

elif valute_one == "USD":
    if valute_two == "USD":
        print(f"{num * usd_usd:.2f}", "USD")
    elif valute_two == "BGN":
        print(f"{num * usd_bgn:.2f}", "BGN")
    elif valute_two == "EUR":
        print(f"{num * usd_eur:.2f}", "EUR")
    elif valute_two == "GBPR":
        print(f"{num * usd_gbp:.2f}", "GBP")

elif valute_one == "EUR":
    if valute_two == "EUR":
        print(f"{num * eur_eur:.2f}", "EUR")
    elif valute_two == "BGN":
        print(f"{num * eur_bgn:.2f}", "BGN")
    elif valute_two == "USD":
        print(f"{num * eur_usd:.2f}", "USD")
    elif valute_two == "GBP":
        print(f"{num * eur_gbp:.2f}", "GBP")

elif valute_one == "GBP":
    if valute_two == "EUR":
        print(f"{num * gbp_eur:.2f}", "EUR")
    elif valute_two == "BGN":
        print(f"{num * gbp_bgn:.2f}", "BGN")
    elif valute_two == "USD":
        print(f"{num * gbp_usd:.2f}", "USD")
    elif valute_two == "GBP":
        print(f"{num * gbp_gbp:.2f}", "GBP")


