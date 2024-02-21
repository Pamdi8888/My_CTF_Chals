# This code might give errors if run on Windows. Use a Unix based OS instead.

from datetime import datetime


with open("timestamps.txt", "r") as file:
    timestamps = file.read().splitlines()
    
# convert the timestamps to datetime objects
for i in range(len(timestamps)):
    timestamps[i] = datetime.strptime(timestamps[i], '%Y-%m-%d %H:%M:%S')
numbers = []

# convert the datetime objects to numbers
for i in range(len(timestamps)):
    # Add your local timezone offset to the timestamp (That is the difference of your local time with UTC in seconds).
    # We do this because the timestamp is in UTC, but the function does calculations in our local time.
    numbers.append(int(timestamps[i].timestamp())+19800)

# for i in range(len(numbers)):
#     print(f"{numbers[i]}: {timestamps[i]}") 

# append all the integers together to form a single number
number = ""
for i in range(len(numbers)):
    number += str(numbers[i])
print(number)

# write output in output.txt
with open("output.txt", "w") as file:
    file.write(number)
