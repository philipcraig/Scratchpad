import time  # we need this for the sleep statement below

# input the limit and convert it to an integer
limit = int(input("What number shall I square up until? "))

# loop from 1 until limit, including limit itself
for i in range(1, limit+1):
    print(i, "squared is", i * i)


# input the number of the times-table and convert it to an integer
table = int(input("Which times-table shall I produce? "))

# loop from 1 until 12, printing each times-table line
for i in range(1, 13):
    print(i, "times", table, "equals", i * table)


total = 0  # total is our running total
next = -1  # Set next to -1 to stop the test beow finishing immediately

# loop until the user's last input was 0
while next != 0:
    # get user's next input
    next = int(input("Next number to add (Enter 0 to quit): "))
    total += next  # add to our running total

print ("The total is", total)


counter = 10  # start counting from 10
while counter > -1:  # while we haven't reached limit
    print(counter, "to go!")  # print our current state
    time.sleep(1)  # Wait 1 second
    counter -= 1  # decrease counter

print ("Bang!")  # explode
