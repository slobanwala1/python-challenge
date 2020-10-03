import os
import csv

# Path to collect data from the Resources folder

budget_data_csv = os.path.join('..', 'PyBank/Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    profit = []
    months_and_date = []
    profit_change = []
    
    # Loop through the data
    
    for row in csvreader:
        profit.append(int(row[1]))
        months_and_date.append(row[0])

    # Get length of months_and_date list
    
    total_months = len(months_and_date)
    
    # Net total amount of profit/losses
    
    net_total = sum(profit)
    
    # Avg change in profit/losses over the entire period/file
    # Basically cur month  val - prev month and add the change to list and keep going down 
    # then divide that by the length
    # Start with first value so you dont subtract first val with null
    
    for val in range(1, len(profit)):
        profit_change.append((int(profit[val]) - (int(profit[val-1]))))
    
    profit_average = sum(profit_change) / len(profit_change)
    
    # Greatest profit increase and decrease over the entire period/file use profit_change
    
    greatest_profit_increase = max(profit_change)
    greatest_profit_increase_month = months_and_date[profit_change.index(max(profit_change))+1]
    greatest_profit_decrease = min(profit_change)
    greatest_profit_decrease_month = months_and_date[profit_change.index(min(profit_change))+1]
    
    # Print statements:
    
    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(total_months))
    print('Total: $' + str(net_total))
    print('Average Change: $' + str(round(profit_average, 2)))
    print('Greatest Increase in Profits: ' + str(greatest_profit_increase_month ) + ' $(' + str(greatest_profit_increase) + ')')
    print('Greatest Decrease in Profits: ' + str(greatest_profit_decrease_month ) + ' $(' + str(greatest_profit_decrease) + ')')
    
    
    # Write output to file
    
    financial_analysis = os.path.join('..', 'PyBank/analysis', 'Financial_analysis.txt')
    
    file = open(financial_analysis, 'w')
    
    file.write('Financial Analysis')
    file.write('\n')
    file.write('----------------------------')
    file.write('\n')
    file.write('Total Months: ' + str(total_months))
    file.write('\n')
    file.write('Total: $' + str(net_total))
    file.write('\n')
    file.write('Average Change: $' + str(round(profit_average, 2)))
    file.write('\n')
    file.write('Greatest Increase in Profits: ' + str(greatest_profit_increase_month ) + ' $(' + str(greatest_profit_increase) + ')')
    file.write('\n')
    file.write('Greatest Decrease in Profits: ' + str(greatest_profit_decrease_month ) + ' $(' + str(greatest_profit_decrease) + ')')
    file.write('\n')
    file.close()

    
    