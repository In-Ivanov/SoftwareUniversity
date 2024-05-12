companies = {}

while True:
    data = input()
    if data == "End":
        break

    company, employee_id = data.split("->")

    if company not in companies:
        companies[company] = [employee_id]

    companies[company].append(employee_id) if employee_id not in companies[company] else ...


for company, employee in companies.items():
    print(company)
    for employee_id in employee:
        print(f"--{employee_id}")


