import threading
import time

# Welcome message
regularTime = time.ctime()
print("Hey! Nice to see you again, today's date is " + regularTime + ".")

# Main Function to count the amount of time to until you walk up again.
def timer():
    y = float(x)
    if y > 0:
        newTime= y*60.0
        print("Time to take a break!")
        time.sleep(newTime)
        print("Good Job Come Back!")
    elif y < 0:
        print("Please enter a positive number.")

# Try function to get the time
try:
    x = input("How long are you planning to work today? ")
except ValueError:
    print("Please enter a number.")
finally:
        timer()
