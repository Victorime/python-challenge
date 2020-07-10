import os

# Module for reading CSV files
import csv
from statistics import mean
csvpath = os.path.join("PyBank/Resources", "budget_data.csv")
outputpath = os.path.join("PyBank/Output", "Financial_Analysis_Summary.txt")

# Track some financial parameters
total_month = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract from row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = total_month + 1
    total_net = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        
        #Track the net change
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        #Calculate the greatest increasee
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

# Print the output to terminal
print(output)

# Export the result to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


