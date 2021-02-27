#import modules
import os
import csv

#create some variables 
total_months = 0
month_counter = 0
net_total = 0
average_change = 0
#tutor helped me understand why this is needed
greatest_decrease = 9999999
greatest_increase = -9999999
greatest_increase_date = ''
greatest_decrease_date = ''
total_profit = 0
total_losses = 0



#create file path
csvpath = os.path.join("Resources", "budget_data.csv")

#this allows you to read the file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #store headers here 
    headers = next (csvreader)
    
    #count months
    for row in csvreader: 
        month_counter += 1
        # total proft
        net_total += int(row[1])

        #get greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_date = row[0]

        #get greatest decrease
        if int(row[1]) < greatest_decrease: 
            greatest_decrease = int(row[1])
            greatest_decrease_date = row[0]

# changes over period
average_change = net_total / month_counter      

#print analysis
print("Financial Analysis")
print("------------------------")
print("Total Months:", total_months)
print("Total:", net_total)
print("Average Change:", average_change)
print("Greatest Increase in Profits:", greatest_increase, greatest_increase_date)
print("Greatest Descrease in Profits:", greatest_decrease, greatest_decrease_date)

#create the path for a text file 
outpath = os.path.join("Analysis", "Analysis.txt")

#give you the ability to write the file
with open(outpath, "w") as file:

    #creating the text in the file
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write("Total Months:" + str(total_months) +"\n")
    file.write("Total:"  + str(net_total) + "\n")
    file.write("Average Change:" + str(average_change) + "\n")
    file.write("Greatest Increase in Profits:" + str(greatest_increase) + greatest_increase_date + "\n")
    file.write("Greatest Descrease in Profits:" + str(greatest_decrease) + greatest_decrease_date)







        
        
        
        
        












