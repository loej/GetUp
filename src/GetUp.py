import time
import os

# Welcome message.
print("Welcome to Get Up, today's date is: " + time.ctime() + ".")
print("---------------------------------------------------------------------")


# Converts time and adds total counts to prompt to get up.
def countTime():
    # 20 minutes in seconds.

    twentyMinstoSecs = 1200

    # Input Values. Converts minutes and/or hours to seconds.
    y = float(x)

    i = float(z)
    # Checks floats that are less than 0.
    if y < 0 or i < 0:

        print("Please enter a valid time.")
    hourTime = y * 3600
    minuteTime = i * 60

    # Total seconds added.
    totalSeconds = hourTime + minuteTime

    # Sets total counter or the while loop.
    # Converts the seconds to the amount of times it will notify the user.
    totalCount = (totalSeconds / twentyMinstoSecs)
    totalCount = int(totalCount)

    # If the workflow is less than 20 minutes it won't set a notification
    if totalCount == 0:
        print("Your Workflow is less than 20 minutes.")
    elif not (totalCount < 0):
        # Loops the amount of times a notification will prompt
        print("Time to get to work!")
        while totalCount != 0:
            time.sleep(twentyMinstoSecs)
            print("Time to take a break, Get Up!")
            totalCount -= 1
            if totalCount == 1:
                print("One stretch to go!")
    else:
        print("Please enter a valid time.")


if __name__ == "__main__":

    # Input values from console, try function.
    try:
        print("Please input the time you're going to work today: ")
        x = input("How many hours are you planning to work today? ")
        z = input("How many minutes are you planning to work today? ")
    except ValueError:
        print("Please enter a numerical value.")
    finally:
        countTime()
