country_name = input().split(", ")
capital_cities = input().split(", ")
cap_dict = {k: v for k, v in zip(country_name, capital_cities)}
for k, v in cap_dict.items():
    print(f"{k} -> {v}")

