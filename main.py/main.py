import csv

election_data = "../Resources/election_data.csv"

f = open("PyPoll.txt", "w")

total_votes = 0
candidates = 0
percentage_won = 0
votes_won = 0
winner = 0

with open(election_data,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    

file_name = "PyPoll.txt"
 
with open(file_name, "a") as txt_file:
 
   txt_file.write("Election Results\n")
   txt_file.write("---------------\n")
 
   txt_file.write(f"Total Votes {total_votes}\n")
   txt_file.write("---------------\n")
 
   txt_file.write(f"Khan: {percentage_won}\n {votes_won}\n")

   txt_file.write(f"Correy: {percentage_won}\n {votes_won}\n")

   txt_file.write(f"Li: {percentage_won}\n {votes_won}\n")

   txt_file.write(f"O'Tooley: {percentage_won}\n {votes_won}\n")
   txt_file.write("---------------\n")
 
   txt_file.write(f"Winner: {winner}\n")
 
file_name = "PyPoll.txt"

