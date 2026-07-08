import datetime, bday_messages

today = datetime.date.today()

next_birthday = datetime.date(today.year, 11, 14)


print(f"Next birthday: {next_birthday}")
print(f"Today's date: {today}")


days_away = (next_birthday - today).days

print(f"Days until next birthday: {days_away}")