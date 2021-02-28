#import modules 
import os
import csv

#here lies the variables


#create file path
csvpath = os.path.join("Resources", "election_data.csv")

#this allows you to read the file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #store headers here 
    headers = next (csvreader)

    for row in csvfile:
        print(row)

#hello 


