import csv

election_data = "../Resources/election_data.csv"

f = open("PyPoll.txt", "w")
 
total_votes = 0
candidate_name = 0
percentage_won = 0
votes_won = 0
most_votes = 0
candidates = {}
candidate_list = []

# candidates = {candidate_name, votes_won, percentage_won}
# candidates = dict()
# candidates = {"name": candidate_name, "votes won": votes_won, "percentage won": percentage_won}


with open(election_data,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # candidates = {"name": candidate_name, "votes won": votes_won, "percentage won": percentage_won}
    # def candidates(election_data):
    # # For readability, it can help to assign your values to variables with descriptive names
    #   candidate_name = str(row[2])
    #   votes_won = int(election_data[1]
      

    for row in csvreader:
      
      candidate_name = row[2]

      total_votes = total_votes + 1
      
      # percentage_won = percentage_won + 1
      # percentage_won = (votes_won / total_votes) * 100
      # print(percentage_won)
      
      # most_votes = most_votes + 1

      # def candidates{
      #   candidate_name = row[2],
      #   votes_won = 
      #   percentage_won}

      if candidate_name in candidates:
        candidates[candidate_name] = candidates[candidate_name] + 1
      else:
        candidates[candidate_name] = 1
        print(candidates)
        
        # if votes_won in most_votes:
        #   most_votes[votes_won] = most_votes[votes_won] + 1
        # else:
        #  most_votes[votes_won] = 1
         
  #  candidate_list[
  #    candidate_name  votes_won
    #  Khan: 2218231
    # Correy: 704200
      # Li: 492940
      # O'Tooley: 105630
    # for key, value in candidates.items():
    #   if value > most_votes:
    #     candidate_name = key
    #     most_votes = value
        
# candidates = dict()

# candidates = {"name": candidate_name), ("vote's won": votes_won), ("percentage won": percentage_won)}
file_name = "PyPoll.txt"
 
with open(file_name, "a") as txt_file:
 
    txt_file.write("Election Results\n")
    txt_file.write("---------------\n")
 
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("---------------\n")
   
    for k, v, in candidates.items():
         txt_file.write(str(k) + ": " + str(v) + "\n")
  
    txt_file.write("---------------\n")

    # for k, v, in most_votes.items():
    #    txt_file.write(str(k) + ": " + str(v) + "\n\n")

    txt_file.write(f"Winner: {most_votes}\n")
 
file_name = "PyPoll.txt"

