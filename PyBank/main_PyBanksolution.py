# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output 

budget_data = os.path.join("Resources", "budget_data.csv")  # Input file path

# Define variables to track the financial data
total_months = []
total_net = 0

# Add more variables to track other necessary financial data

profit_loss_changes = []
count_months = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Open and read the csv
with open(budget_data,'r') as financial_data:

    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    #print(f"Header: {header}")
    # This prints -->> Header: Date, Profit/Losses

    # Extract first row to avoid appending to net_change_list
    next(reader)

    # Track the total and net change
    

    # Process each row of data
    for row in reader:
        profit_loss=float(row[1])

        # Count of months
        count_months += 1

        # Track the total
        current_month_profit_loss = int(row[1])
        total_net += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue
        else:

        # Track the net change
            # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            total_months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)


    # Calculate the greatest increase in profits (month and amount)
    best_month = total_months[highest_month_index]

    # Calculate the greatest decrease in losses (month and amount)
    worst_month = total_months[lowest_month_index]


# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${total_net}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

# Export a text file with the results
output_file = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Write the results to a text file
with open(output_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${total_net}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")