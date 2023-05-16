import os
import csv

#Set path for file
csvpath = os.path.join(".","Resources","budget_data.csv")

#Open csv file
with open(csvpath,encoding = 'UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")

        header = next(csvreader)

#Variables
        total = 0
        total_change = 0
        prev = 0
        max_increase = 0
        max_date = ""
        max_decrease = 0
        min_date =""
        on_first_row = True

#Calculations
        for row in csvreader:
                curr = int(row[1])
                total += curr
                change = 0
                if not on_first_row:      
                        change = curr - prev
                        total_change += change
                        if change > max_increase:
                                max_increase = change
                                max_date = (row[0])
                
                        if change < max_decrease:
                                max_decrease = change
                                min_date = (row[0])
                else:
                        on_first_row = False
                prev = curr

    
        total_months = csvreader.line_num-1
        ave = total_change / (total_months-1)

#Print to Terminal        
print("Financial Analysis")
print("-------------------------")
print("Total Months: %d" %(total_months))
print("Total: $%d" %(total))
print("Average Change: $"+"{:.2f}".format(ave))
print("Greatest Increase in Profits: %s ($%d)" %(max_date, max_increase))
print("Greatest Decrease in Profits: %s ($%d)" %(min_date, max_decrease))

#Create Text File
with open("out.txt", "w") as f:
        f.write("Financial Analysis")
        f.write("\n")
        f.write("-------------------------")
        f.write("\n")
        f.write("Total Months: %d" %(total_months))
        f.write("\n")
        f.write("Total: $%d" %(total))
        f.write("\n")
        f.write("Average Change: $"+"{:.2f}".format(ave))
        f.write("\n")
        f.write("Greatest Increase in Profits: %s ($%d)" %(max_date, max_increase))
        f.write("\n")
        f.write("Greatest Decrease in Profits: %s ($%d)" %(min_date, max_decrease))

      
      
