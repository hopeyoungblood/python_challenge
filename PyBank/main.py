import csv

budget_data = "../Resources/budget_data.csv"

f = open("PyBank.txt", "w")

current = 0
first = 0
last = 0
months = 0
total_change = 0
total_months = 0
num_months = []
profits_losses = []
average_change = 0
greatest_increase = 0
greatest_decrease = 0


with open(budget_data,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # profits_losses.append(total_change)
    # print(profits_losses)

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        
        total_months = total_months + 1
        print(total_months)
        
        total_change = total_change + int(row[1])
        print(total_change)

        average_change = (last - first) / total_months
        print(average_change)

        # profits_losses.append(total_change)
        # print(profits_losses)

        # # # step two just find the difference between the two months
        current = int(row[1])

        if months > 1:
            change = current - last
            print(change)  

            total_months = total_months + 1
            print(total_months) 

            total_change = total_change + change
            print(total_change)

            average_change = (last - first) / (total_months + 1)
            print(average_change)

        last = int(row[1])
        print(last)

        # num_months.append = total_months
        # print(num_months)

        # profits_losses.append(total_change)
        # print(profits_losses)
            
        # greatest_increase = 
        # greatest_decrease = 
    
file_name = "PyBank.txt"

with open(file_name, "a") as txt_file:

    txt_file.write("Financial Analysis\n")
    
    txt_file.write("---------------\n")
    
    txt_file.write(f"Total Months: {total_months}\n")
    
    txt_file.write(f"Net Total: ${total_change}\n")
     
    txt_file.write(f"Average Change: ${average_change}\n")

    txt_file.write(f"Greatest Increase in Profits: {greatest_increase}\n")

    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease}\n")

file_name = "PyBank.txt"
