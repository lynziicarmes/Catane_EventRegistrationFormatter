first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event = input("Enter event name: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

full_name = first_name + " " + last_name

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Section:", section)
print("Event:", event)
print("Event Date:", month, day + ",", year)