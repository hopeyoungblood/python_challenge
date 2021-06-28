import csv

budget_data = "../Resources/budget_data.csv"

f = open("PyBank.txt", "w")

# total = int(row[1])
total_profit_losses = 0
current = 0
last = 0
total_change = 0
months = 0
net_total = 0
total_months = 0
average_change = 0

with open(budget_data, 'r') as csvfile:
    
   # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        total_months = total_months + 1
        print(total_months)

        net_total = net_total + int(row[1])
        print(net_total)

        total_profit_losses = total_profit_losses + int(row[1])
        print(total_profit_losses)

        average_change = total_change / (total_months) * 100
        print(average_change)

        # # # step two just find the difference between the two months
        current = int(row[1])

        if months > 1:
             change = current - last
             print(change)
            
             total_change = total_change + change
             print(total_change)
            
             last = int(row[1])
             print(last)
        
             average_change = total_change / (months - 1) 
             print(average_change)

file_name = "PyBank.txt"

with open(file_name, "a") as txt_file:


    txt_file.write("Financial Analysis\n")
    txt_file.write("---------------\n")

    txt_file.write(f"Total Months: {total_months}\n")

    txt_file.write(f"Net Total: {net_total}\n")

    # txt_file.write(f"Total Change: {total_change}\n")

    txt_file.write(f"Average Change: {average_change}\n")

    # txt_file.write(f"{second_place}: {second_place_results}\n")

file_name = "PyBank.txt"

# first_place = "Bob"
# first_place_results = 100

# second_place = "Sally"
# second_place_results = 100


