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
#need list of candidates
candidates = ['Khan', 'Correy', 'Li', "O'tooley"]
candidate_votes = []


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
        elif row[2] == "O'Tooley":
            otooley_votes += 1

total_votes = str(vote_counter)

#get percent of votes
percent_khan = round(int(khan_votes)/int(vote_counter)*100)
percent_correy = round(int(correy_votes)/int(vote_counter)*100)
percent_li = round(int(li_votes)/int(total_votes)*100)
percent_otooley = round(int(otooley_votes)/int(total_votes)*100)



#determine winner 
#winner = 

#need to print out some results
print("Election Results")
print("---------------------")
print("Total Votes: " + total_votes)
print("Khan: " + str(percent_khan) + "% " + str(khan_votes))
print("Correy : " + str(percent_correy) + "% " + str(correy_votes))
print("Li :" + str(percent_li) + "% " + str(li_votes))
print("O'tooley: " + str(percent_otooley) + "% " + str(otooley_votes))
print("---------------------------------")
print("Winner: ")
print("----------------------------------")


#create the path for a text file 
outpath = os.path.join("Analysis", "Analysis.txt")

#give you the ability to write the file
with open(outpath, "w") as file:

    file.write("Election Results\n")
    file.write("------------------------------\n")
    file.write("Total Votes: " + total_votes + "\n")
    file.write("Khan: " + str(percent_khan) + "% " + str(khan_votes) + "\n")
    file.write("Correy : " + str(percent_correy) + "% " + str(correy_votes) + "\n")
    file.write("Li :" + str(percent_li) + "% " + str(li_votes) + "\n")
    file.write("O'tooley: " + str(percent_otooley) + "% " + str(otooley_votes) + "\n")
    file.write("---------------------------------\n")
    file.write("Winner: \n")
    file.write("----------------------------------\n")


