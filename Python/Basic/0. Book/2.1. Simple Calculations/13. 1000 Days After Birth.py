from datetime import datetime, timedelta

birthdate_input = input()

birthdate = datetime.strptime(birthdate_input, '%d-%m-%Y')

result_date = birthdate + timedelta(days=999)

result_date_str = result_date.strftime('%d-%m-%Y')
print(result_date_str)






