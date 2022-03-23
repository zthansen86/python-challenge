#Import Modules
import os
import csv

#Set Path for File
pybank_data = os.path.join("..", "\\PyBank\Resources", "budget_data.csv")

#Set each variable and store as a list
#Total count of months in the data set
date = []

#Net total amount of profit/losses in data set
profit_losses = []

#Open and Read csv File
with open(pybank_data) as csv_file:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read header row first
    csvheader = next(csvreader)

    #Add date to python list
    date.append(row[0])

    #Add profit_losses to python list
    profit_losses.append(int(row[1]))

#Create new variable to hold value for total number of rows (months) in the date list
total_months = len(date)

#Create new variable to hold sum of profit_losses list and format to dollars
total_profit_losses = "${}".format(sum(profit_losses))

#Create new placeholder to store the list of differences in profit_losses for next loop
difference_list = []

#Loop through to compare adjoining values in profit_losses list
for row in range(total_months - 1):
    first_number = profit_losses[row]
    second_number = profit_losses[row+1]

    #Create new variable to calculate difference between adjoining values
    difference = second_number - first_number

#New variable is generated from the calculation  which determines average of difference of adjoining values and is formatted for dollars and cents
average = "${:,.2f}".format((sum(difference_list)) / len(difference_list))

#Create new variable to hold maximum value in difference_list
greatest_increase = max(difference_list)

#Create new variable to hold index of greatest increase in difference_list
greatest_increase_index = difference_list.index(greatest_increase)

#Create new variable to hold date using index from above step
greatest_date = date[greatest_increase_index + 1]

#Format variable for dollars
greatest_increase = "${}".format(greatest_increase)

#Create same variables as above but for decreases
#Create new varaible to hold minimum value in difference_list
greatest_decrease = min(difference_list)

#Create new variable to hold index of greates decrease in difference_list
greatest_decrease_index = difference_list.index(greatest_decrease)

#Create new variable to hold date using index from above step
greatest_decrease_date = date[greatest_decrease_index + 1]

#Format variables for dollars
greatest_decrease = "${}".format(greatest_decrease)

#Print results
print("Financial Analysis")
print("---------------------------")
print(f'Total Months: {total_months}')
print(f'Total: {total_profit_losses} ')
print(f'Average Change: {average}')
print(f'Greatest Increase in Profits: {greatest_date} ({(greatest_increase)})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} ({(greatest_decrease)})')




    



