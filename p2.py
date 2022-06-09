########################## FUNCTIONS ################################

def leapYear(y):
    # check if a year "y" is leap year or not
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True


def getDate():
    # validate integers
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


########################## MAIN ################################

#months  	 [ja, fe, ma, ap, ma, ju, ju, au, se, oc, no, dec]
days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#             [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]

while True:
    # ask user for a date
    day, month, year = getDate()

    # checking if the chosen year is leap or not and add 1 day to february if so
    if leapYear(year) == True:
        days_month[1] = 29
    else:
        days_month[1] = 28

    # validating dates and calculating days
    if day <= days_month[month-1] and day > 0 and month > 0 and month <= 12:
        days = (sum(days_month[:month-1])) + day
        print("Your chosen date is the day number", days, "of the year")
    else:
        print("Please enter a valid date")
        continue

    # play again?
    while True:
        play_again = input("To try again press \"Y\" or \"N\" to quit ")
        if play_again == "Y":
            break
        elif play_again == "N":
            print("Thanks for your time! See you next time")
            quit()
        else:
            print("Please press \"Y\" to try again or \"N\" to quit")
