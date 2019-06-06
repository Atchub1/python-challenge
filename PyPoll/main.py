import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0 
    otooley_votes = 0

    #getting total votes for each candidite 
    for row in csvreader:
        if row[2] == 'Khan':
            khan_votes = khan_votes + 1
        if row[2] == 'Correy':
            correy_votes = correy_votes + 1
        if row[2] == 'Li':
            li_votes = li_votes + 1
        if row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
        
    # print(khan_votes)

    #calculating total votes cast
    total_votes  = khan_votes + correy_votes + li_votes + otooley_votes
    print(total_votes)


#calculating percentage of vote for each candidate
khan_vote_pct = '{0:.3f}'.format((khan_votes/total_votes)*100)
correy_vote_pct = '{0:3f}'.format((correy_votes/total_votes)*100)
li_vote_pct = '{0:.3f}'.format((li_votes/total_votes)*100)
otooley_vote_pct = '{0:.3f}'.format((otooley_votes/total_votes)*100)
#print(khan_vote_pct)

#find the winner
if khan_vote_pct > correy_vote_pct and li_vote_pct and otooley_vote_pct:
    winner = 'Khan'
    # print(winner)

if correy_vote_pct > khan_vote_pct and li_vote_pct and otooley_vote_pct:
    winner = 'Correy'
    # print(winner)

if li_vote_pct > correy_vote_pct and khan_vote_pct and otooley_vote_pct:
    winner = 'Li'
    # print(winner)

if otooley_vote_pct > correy_vote_pct and otooley_vote_pct > li_vote_pct and otooley_vote_pct > khan_vote_pct:
    winner = "O'Tooley"
    # print(winner)


#printing results in list
election_results = 'Election Results'
line_break = '-------------------------'
total_vote_statement = f'Total Votes: {total_votes}'
khan_vote_statement = f'Khan: {khan_vote_pct}% ({khan_votes})'
correy_vote_statement = f'Correy: {correy_vote_pct}% ({correy_votes})'
li_vote_statement = f'Li: {li_vote_pct}% ({li_votes})'
otooley_vote_statement = f"O'Tooley: {otooley_vote_pct}% ({otooley_votes})"
winner_statement = f'Winner: {winner}'
result_list = [election_results, line_break, total_vote_statement, line_break, khan_vote_statement, correy_vote_statement, li_vote_statement, otooley_vote_statement, line_break, winner_statement, line_break]

# print(khan_vote_statement)


#printing to terminal and txt file
file = open('Election Results.txt', 'w')
for i in result_list:
    file.write(i)
    file.write("\n") 
    print(i)

file.close()