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
net_total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 99999


with open(budget_data,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        net_total = net_total + int(row[1])
        
        total_months = total_months + 1
        print(total_months)

        current = int(row[1])

        # # # step two just find the difference between the two months
       
        if total_months > 1:
            change = current - last
            print(change)  

            # total_months = total_months + 1
            # print(total_months) 

            total_change = total_change + change
            print(total_change)

            average_change = total_change / (total_months - 1)
            print(average_change)
            
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = str(row[0])

            if change < greatest_decrease:
                greatest_decrease = change  
                greatest_decrease_month = str(row[0])

        last = int(row[1])
        print(last)
    
file_name = "PyBank.txt"

with open(file_name, "a") as txt_file:

    txt_file.write("Financial Analysis\n")
    
    txt_file.write("---------------\n")
    
    txt_file.write(f"Total Months: {total_months}\n")
    
    txt_file.write(f"Net Total: ${net_total}\n")
     
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

file_name = "PyBank.txt"
