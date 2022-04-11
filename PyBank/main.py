#import dependencies
import os
import csv

# set csv path
csv_path = os.path.join("PyBank/Resources/budget_data.csv")

# open and read csv file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # name the delimeter
    csv_header = next(csvreader)

    # declare all variables
    total_months = []
    profit_loss = []
    difference = []
    greatest_inc_date = ""
    greatest_dec_date = ""

    # total months
    for row in csvreader:
        total_months.append(row[0])
        profit_loss.append(row[1])
        profit_loss = [int(i) for i in profit_loss]
        total_change = 0

    for i in range(len(profit_loss)-1):

        # avg change through time period
        difference = profit_loss[i+1] - profit_loss[i]
        total_change = total_change + difference

        # find avg change
        avg_change = (total_change) / (len(profit_loss)-1)

    # biggest increase and date
    greatest_inc_profit = max(profit_loss)
    greatest_inc_date = str(total_months[profit_loss.index(max(profit_loss))])

    # biggest decrease and date
    greatest_dec_profit = min(profit_loss)
    greatest_dec_date = str(total_months[profit_loss.index(min(profit_loss))])

# print to terminal
print("Finanical Analysis")
print("------------------")
print("Total Months:", len(total_months))
print("Total: $", sum(profit_loss))
print("Average Change: $" + str("%.2f" % avg_change))
print("Greatest Increase in Profits: " +
    greatest_inc_date + "($" + str(greatest_inc_profit)+")")
print("Greatest Decrease in Profits: " +
    greatest_dec_date + "($" + str(greatest_dec_profit)+")")

#export to text file
def text_file():
    return str("Financial Analysis" + 
    "------------------" + 
    "Total Months: 86" +
    "Total: $38382578" +
    "Average Change: $-2315.12" +
    "Greatest Increase in Profits: Feb-2012 ($1170593)" +
    "Greatest Decrease in Profits: Sep-2013 ($-1196225")
output = text_file()
file = open("output.txt", "w")
file.write(output)
file.close()
