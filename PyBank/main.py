## PyBank

# Dependencies
import csv
import os

# Read csv file
csvpath = os.path.join(Resources)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row and add to list
    csv_budget = []
    csv_budget = next(csvreader)

    # Read each row of data after the header and add to list
    for row in csvreader:
        csv_budget.append(row)

#print(csv_budget[2:])

# The total number of months included in the dataset
print(f"There are {len(csv_budget)-2} months included in the dataset")

# The net total amount of "Profit/Losses" over the entire period
profit_count = 0
loss_count = 0
for month in csv_budget[2:]:
    if month > 0: profit_count += 1
    else:loss_count += 1

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period