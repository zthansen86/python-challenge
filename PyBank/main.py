#import dependencies
import os
import csv

#set csv path
pybank_path = os.path.join('..', 'Resources', 'budget_data.csv')

#open and read csv file
with open(pybank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #name the delimeter
    csv_header = next(csvreader)

    #declare all variables
    total_months = []
    profit_loss = []
    difference = []
    greatest_inc_date = ""
    greatest_dec_date= ""

    #total months
    for row in csvreader:
        total_months.append(row[0])
        profit_loss.append(row[1])
        profit_loss = [int(i) for i in profit_loss]
        total_change =0
    
    for i in range(len(profit_loss)-1):

        #avg change through time period
        difference = profit_loss[i+1] - profit_loss[i]
        total_change = total_change + difference

        #find avg change
        avg_change = (total_change) / (len(profit_loss)-1)

    #biggest increase and date
    greatest_inc_profit = max(profit_loss)
    greatest_inc_date = str( total_months[profit_loss.index(max(profit_loss))])

    #biggest decrease and date
    greatest_dec_profit = min(profit_loss)
    greatest_dec_date = str( total_months[profit_loss.index(min(profit_loss))])

#print to terminal
print("Finanical Analysis")
print("------------------")
print("Total Months:", len(total_months))
print("Total: $", sum(profit_loss))
print("Average Change: $" + str("%.2f" % avg_change))
print("Greatest Increase in Profits: " + greatest_inc_date + "($" + str(greatest_inc_profit)+")")
print("Greatest Decrease in Profits: " + greatest_dec_date + "($" + str(greatest_dec_profit)+")")
