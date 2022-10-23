from datetime import datetime
import locale


print("The Hotel Reservation Program\n")

again = "y"
while again.lower() == "y":
    #get guest date of arrival
    while True:
        date_string = input("Enter arrival date using format (YYYY-MM-DD):  ")
        try:  
            arrival_date = datetime.strptime(date_string, "%Y - %m -%d")
        except valueError:
            print("Invalid date format. Try again.")
            print

        #strip non-zero time values from datetime)
        now = datetime.now()
        today= datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print("Arrival date must be today or later. Try again.")
            print()
        else:
            break

        while True:
            date_string=input("Enter departure date(YYYY-MM-DD): ")
        try:
            departure_date=datetime.strptime(date_string, "%Y - %m -%d")
                except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue #skip next if statment and restart loop.
        if departure_date <= arrival_date:
            print("Departure must be after arrival date. Try again.")
            print()
        else:
            break

