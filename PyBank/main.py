import os
import csv

pybank_budget_data=os.path.join('Resources', 'budget_data.csv')

# use below to use absoulte path to budget data csv
#pybank_budget_data=os.path.join("<path to csv file>")


# open the data file
with open(pybank_budget_data, newline="") as budget_data_file:
    csvreader = csv.reader(budget_data_file, delimiter=",")
    # Read header row
    budget_data_file_header = next(csvreader)

    # Initialize required variables
    first_row_amount = 0
    second_row_amount = 0
    net_total_amount = 0
    
    total_months = 0
    
    monthly_change = 0
    monthly_changes = []
    
    dates =[]

    first_row = next(csvreader)
    first_row_amount = int(first_row[1])
    # for loop to loop thorough rows
    for row in csvreader:

        second_row_amount = int(row[1])
        monthly_change = second_row_amount - first_row_amount
        monthly_changes.append(monthly_change)
        first_row_amount = second_row_amount
        
        total_months += 1
        net_total_amount += int(row[1])
        dates.append(row[0])

    # calculate average    
    average_change = round (sum(monthly_changes)/len(monthly_changes),2)

    # calculate max increase 
    max_increase = max(monthly_changes)   
    max_increase_month = dates[monthly_changes.index(max_increase)]
    # calculate max decrese 
    max_decrease = min(monthly_changes)
    max_decrease_month = dates[monthly_changes.index(max_decrease)]

    # print to console
    print(f"Financial Analysis\n")
    print(f"----------------------------\n")
    print(f"Total Months: {str(total_months)}\n")
    print(f"Total: ${str(net_total_amount)}\n")
    print(f"Average Change: ${str(average_change)}\n")
    print(f"Greatest Increase in Profits: {max_increase_month} (${str(max_increase)})\n")
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${str(max_decrease)})\n")

# Export to file
output_file = os.path.join('python-challenge/PyBank/analysis', 'pyBank_output.txt')
#use below to use absolute path
#output_file = os.path.join('<path to file>', 'pyBank_output.txt')

pyBankAnalysis = open(output_file, "w")


lines = []
# append to lines 
lines.append("Financial Analysis\n")
lines.append("----------------------------\n")
lines.append(f"Total Months: {str(total_months)}\n")
lines.append(f"Total: ${str(net_total_amount)}\n")
lines.append(f"Average Change: ${str(average_change)}\n")
lines.append(f"Greatest Increase in Profits: {max_increase_month} (${str(max_increase)})\n")
lines.append(f"Greatest Decrease in Profits: {max_decrease_month} (${str(max_decrease)})\n")
# write lines
pyBankAnalysis.writelines(lines)
pyBankAnalysis.close