all_pages = int(input())
pages = int(input())
days = int(input())

book_hours = all_pages / pages
day_hours = book_hours / days
print(int(day_hours))
