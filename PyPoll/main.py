#import modules 
import os
import csv

#here lie the variables
vote_counter = 0
total_votes = 0
#variables to track candidates and their votes 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
#variables to track their percent of votes
percent_khan = 0
percent_correy = 0
percent_li = 0
percent_otooley = 0 
winner = ""





#create file path
csvpath = os.path.join("Resources", "election_data.csv")

#this allows you to read the file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #store headers here 
    headers = next (csvreader)

    #count votes
    for row in csvreader:
        vote_counter += 1
        #count votes for each candidate
        if row[2] == 'Khan':
            khan_votes += 1
        elif row[2] == 'Correy':
            correy_votes += 1
        elif row[2] == 'Li':
            li_votes += 1
        elif row[2] == "O'tooley":
            otooley_votes += 1




