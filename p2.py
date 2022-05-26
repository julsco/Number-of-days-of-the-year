# Function to Get the date from the user

def getDate():
    while True:
        try:
            day = int(input("Please enter the day: "))
            break
        except:
            print("Please enter a valid day")
    while True:
        try:
            month = int(input("Please enter the month: "))
            break
        except:
            print("Please enter a valid month")
    while True:
        try:
            year = int(input("Please enter the year: "))
            break
        except:
            print("Please enter a valid year")
    return (day, month, year)

# Function to check if year is common or leap


def leapYear(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True

# Creating 1 list for each month of the year


january = list(range(1, 32))
february = list(range(1, 29))
march = list(range(1, 32))
april = list(range(1, 31))
may = list(range(1, 32))
june = list(range(1, 31))
july = list(range(1, 32))
august = list(range(1, 32))
september = list(range(1, 31))
october = list(range(1, 32))
november = list(range(1, 31))
december = list(range(1, 32))

# Creating variables to add number of days from beggining of the year until beginning of each month

jan_to_feb = len(january) + len(february)
jan_to_mar = jan_to_feb + len(march)
jan_to_apr = jan_to_mar + len(april)
jan_to_may = jan_to_apr + len(may)
jan_to_jun = jan_to_may + len(june)
jan_to_jul = jan_to_jun + len(july)
jan_to_aug = jan_to_jul + len(august)
jan_to_sep = jan_to_aug + len(september)
jan_to_oct = jan_to_sep + len(october)
jan_to_nov = jan_to_oct + len(november)

# Main while

while True:
    day, month, year = getDate()

    if leapYear(year) == True:
        february = list(range(1, 30))

    if year < 0:
        print("Please enter a valid date")
        continue

    if month == 1:
        days = 0
        if day not in january:
            print("Please enter a valid date")
            continue

    elif month == 2:
        days = len(january)
        if day not in february:
            print("Please enter a valid date")
            continue

    elif month == 3:
        days = jan_to_feb
        if day not in march:
            print("Please enter a valid date")
            continue

    elif month == 4:
        days = jan_to_mar
        if day not in april:
            print("Please enter a valid date")
            continue

    elif month == 5:
        days = jan_to_apr
        if day not in may:
            print("Please enter a valid date")
            continue

    elif month == 6:
        days = jan_to_may
        if day not in june:
            print("Please enter a valid date")
            continue

    elif month == 7:
        days = jan_to_jun
        if day not in july:
            print("Please enter a valid date")
            continue

    elif month == 8:
        days = jan_to_jul
        if day not in august:
            print("Please enter a valid date")
            continue

    elif month == 9:
        days = jan_to_aug
        if day not in september:
            print("Please enter a valid date")
            continue

    elif month == 10:
        days = jan_to_sep
        if day not in october:
            print("Please enter a valid date")
            continue

    elif month == 11:
        days = jan_to_oct
        if day not in november:
            print("Please enter a valid date")
            continue

    elif month == 12:
        days = jan_to_nov
        if day not in december:
            print("Please enter a valid date")
            continue

    elif month <= 0 or month > 12:
        print("Please enter a valid date")
        continue

    # Printing result depending if the year is leap or not

    if leapYear(year) == True and month > 2:
        print("Your chosen date is the day number",
              days + day + 1, "of the year. Leap year")
    else:
        print("Your chosen date is the day number", days + day, "of the year")

    # Play again?

    while True:
        play_again = input("To try again press \"Y\" or \"N\" to quit ")
        if play_again == "Y":
            break
        elif play_again == "N":
            print("Thanks for your time! See you next time")
            quit()
        else:
            print("Please press \"Y\" to try again or \"N\" to quit")
