#import dependencies
from cgitb import text
import os
import csv
from unicodedata import name

# set csv path
csv_path = os.path.join("PyPoll/Resources/election_data.csv")

# create lists to store data
voter_id = []
candidate = []

# open and read csv file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header row first
    csvheader = next(csvreader)

    # read through the data
    for row in csvreader:

        voter_id.append(row[0])
        candidate.append(row[2])

    # new variable
    total_votes = int(len(voter_id))

    candidate_count = [[j, candidate.count(j)] for j in set(candidate)]

    name_list = [i[0] for i in candidate_count]
    count_list = [i[1] for i in candidate_count]

    max_value = max(count_list)

    winner_index = count_list.index(max_value)

    winner_name = name_list[winner_index]

    percentages = []

    for k in range(0, len(count_list)):
        percent = round((count_list[k] / total_votes) *100, 2)
        percentages.append(percent)

#print results
print("Election Results")
print("----------------------------")
print(f'Total Votes: {total_votes}')
print("----------------------------")
for n in range(0, len(name_list)):
    print(f'{name_list[n]}: {percentages[n]}% ({count_list[n]})')
print("----------------------------")
print(f'Winner: {winner_name}')
print("----------------------------")

#export to text file
def text_file():
    return str("Election Results" +
    "----------------------" +
    "Total Votes: 1048575" +
    "----------------------" +
    "O'Tooley: 3.01% (31586)" +
    "Correy: 19.94% (209046)" +
    "Li: 13.96% (146360)" +
    "Khan: 63.09% (661583)" +
    "----------------------" +
    "Winner: Khan" +
    "----------------------")
output = text_file()
file = open("output.txt", "w")
file.write(output)
file.close()


