import csv

election_data = "../Resources/election_data.csv"

f = open("PyPoll.txt", "w")

total_votes = 0
candidate_name = 0
percentage_won = 0
votes_won = 0
winner = 0
most_votes = 0
candidates = {}
# candidates = dict()
# candidates = {candidate_name, votes_won, percentage_won}


with open(election_data,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

      candidate_name = row[2]

      total_votes = total_votes + 1
      
      # percentage_won = percentage_won + 1
      percentage_won = votes_won / total_votes
      
      most_votes = votes_won + 1

      if candidate_name in candidates:
        candidates[candidate_name] = candidates[candidate_name] + 1
      else:
        candidates[candidate_name] = 1
    print(candidates)

    # candidates = dict(candidate_name, votes_won, percentage_won)

file_name = "PyPoll.txt"
 
with open(file_name, "a") as txt_file:
 
    txt_file.write("Election Results\n")
    txt_file.write("---------------\n")
 
    txt_file.write(f"Total Votes {total_votes}\n")
    txt_file.write("---------------\n")
   
    for k, v, in candidates.items():
        txt_file.write(str(k) + ": " + str(v) + "\n\n")
  
    txt_file.write("---------------\n")

    # for k, v, in most_votes.items():
    #   txt_file.write(str(k) + ": " + str(v) + "\n\n")

    txt_file.write(f"Winner: {winner}\n")
 
file_name = "PyPoll.txt"

