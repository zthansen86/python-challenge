#Import Modules
import os
import csv

#Set Path for File
pybank_data = os.path.join("..", "PyBank/Resources", "budget_data.csv")

#Set each variable and store as a list
#Total count of months in the data set
date = []

#Net total amount of profit/losses in data set
profit_losses = []

#Open and Read csv File
with open(pybank_data) as csv_file:
    csvreader = csv.reader(csvfile, delimiter=',')
    



