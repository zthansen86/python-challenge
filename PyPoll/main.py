#import dependencies
import os
import csv

# set csv path
csv_path = os.path.join("PyPoll/Resources/election_data.csv")

# open and read csv file
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

# declare variables
candidate_one = "Khan"
candidate_two = "Correy"
candidate_three = "Li"
candidate_four = "O'Tooley"

# variables defined and set to 0
starting_vote_one = 0
starting_vote_two = 0
starting_vote_three = 0
starting_vote_four = 0

# loop through for candidates votes
for row in csv_reader:
    if row[2] == candidate_one:
        starting_vote_one = starting_vote_one + 1
    elif row[2] == candidate_two:
        starting_vote_two = starting_vote_two + 1
    elif row[2] == candidate_three:
        starting_vote_three = starting_vote_three + 1
    elif row[2] == candidate_four:
        starting_vote_four = starting_vote_four + 1

# total votes
total_votes = starting_vote_one + starting_vote_two + \
    starting_vote_three + starting_vote_four

# find out candidate percentages
khan_per = float((starting_vote_one/total_votes)*100)
correy_per = float((starting_vote_two/total_votes)*100)
li_per = float((starting_vote_three/total_votes)*100)
otooley_per = float((starting_vote_four/total_votes)*100)

# print results
Print("Election Results")
Print("-------------------------")
Print("Total Votes: " + str(total_votes))
Print("-------------------------")
Print("Khan" + " " + str("%.3f" % khan_per) +
    "%" + " " + "(" + str(starting_vote_one) + ")")
Print("Correy" + " " + str("%.3f" % correy_per) +
    "%" + " " + "(" + str(starting_vote_two) + ")")
Print("Li" + " " + str("%.3f" % li_per) + "%" +
    " " + "(" + str(starting_vote_three) + ")")
Print("O'Tooley" + " " + str("%.3f" % otooley_per) +
    "%" + " " + "(" + str(starting_vote_four) + ")")
Print("------------------------")

if starting_vote_one > starting_vote_two and starting_vote_one > starting_vote_three and starting_vote_one > starting_vote_four:
    print("Winner: Khan")
elif starting_vote_two > starting_vote_one and starting_vote_two > starting_vote_three and starting_vote_two > starting_vote_four:
    print("Winner : Correy")
elif starting_vote_three > starting_vote_one and starting_vote_three > starting_vote_two and starting_vote_three > starting_vote_four:
    print("Winner: Li")
else:
    print("Winner: O'Tooley")

print("--------------------------")
