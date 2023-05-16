import os
import csv
#Set path for file
csvpath = os.path.join(".","Resources","election_data.csv")

#Open csv file
with open(csvpath,encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#Variables    
    header = next(csvreader)
    total_votes = 0
    candidates = []
    totals = {}
    winning_votes = 0
    winner = ""

#Calculations
    for row in csvreader:
        voter_id = row[0]
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            totals[candidate] = 0
        totals[candidate] += 1
    
    total_votes = csvreader.line_num-1

#Print to Terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: %d" %(total_votes))
    print("-------------------------")
    for candidate in candidates:
        candidate_votes = totals[candidate] 
        if candidate_votes > winning_votes:
            winning_votes = candidate_votes
            winner = candidate
        percentage = candidate_votes/total_votes
        print(candidate + ": " + ("{:.3%}".format(percentage)) + " " + "(" + str(candidate_votes) + ")")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

#Create Text File
with open("out.txt", "w") as f:
    f.write("Election Results")
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write("Total Votes: %d" %(total_votes))
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    for candidate in candidates:
        candidate_votes = totals[candidate] 
        if candidate_votes > winning_votes:
            winning_votes = candidate_votes
            winner = candidate
        percentage = candidate_votes/total_votes
        f.write(candidate + ": " + ("{:.3%}".format(percentage)) + " " + "(" + str(candidate_votes) + ")")
        f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write("Winner: " + winner)
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
        