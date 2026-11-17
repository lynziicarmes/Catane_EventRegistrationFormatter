from datetime import datetime

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event = input("Enter event name: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event = event.strip().title()

full_name = first_name + " " + last_name

date = datetime(year, month, day)

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event)
print("Event Date:", date.strftime("%B"), date.day, ",", date.year)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("\nRegistration record created successfully.")