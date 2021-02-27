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
        net_total += row[1]

        #get greatest increase
        if row[1] > greatest_increase:
            greatest_increase = row[1]
            greatest_increase_date = row[0]

        #get greatest decrease
        if row[1] < greatest_decrease: 
            greatest_decrease = row[1]
            greatest_decrease_date = row[0]

# changes over period
average_change = net_total / month_counter      

#print analysis
print("Financial Analysis")
print("------------------------")
print("Total Months:", total_months)



        
        
        
        
        












