## PyBank

# Dependencies
import csv
import os

# Set file path for csv file and read csv file
csvpath = os.path.join('Resources/budget_data.csv')

csv_file = open(csvpath, 'r')
csv_reader = csv.reader(csv_file)

# skip first row (column headers)
next(csv_reader)
num_months = 0
total_profit = 0
total_change = 0
prev_profit = 0
change = 0
max_change = -float('inf')  # initialize max change to negative infinity
max_change_date = ''
min_change = float('inf')  # initialize min change to positive infinity
min_change_date = ''

for row in csv_reader:
    num_months += 1
    date = row[0]
    profit = float(row[1])
    total_profit += profit

    if num_months > 1:  # only calculate change starting from second month
        change = profit - prev_profit
        total_change += change

    # update maximum and minimum profit values and dates
    if change > max_change:
        max_change = change
        max_change_date = date
    if change < min_change:
        min_change = change
        min_change_date = date
    
    prev_profit = profit  # update previous profit value for next iteration
    
average_change = total_change / (num_months - 1)  # calculate average change

# print analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${int(total_profit)}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_change_date} (${int(max_change)})")
print(f"Greatest Decrease in Profits: {min_change_date} (${int(min_change)})")
print("----------------------------")

# export a text file with the results
with open('analysis/output.txt', 'w') as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f"Total Months: {num_months}", file=f)
    print(f"Total: ${int(total_profit)}", file=f)
    print(f"Average Change: ${average_change:.2f}", file=f)
    print(f"Greatest Increase in Profits: {max_change_date} (${int(max_change)})", file=f)
    print(f"Greatest Decrease in Profits: {min_change_date} (${int(min_change)})", file=f)
    print("----------------------------", file=f)