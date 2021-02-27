#import modules
import os
import csv

#create some variables
total_months = 0
month_counter = 0
net_total = 0
average_change = 0
greatest_decrease = 0
greatest_increase = 0
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
        
        
        
        
        


# changes over period
average_change = net_total / month_counter        









