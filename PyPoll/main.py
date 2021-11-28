#import libraries
import os
import csv

#define a path variable using os.path.join to allow for reading on different os
pypoll_src_path = os.path.join(".","Resources","election_data.csv")

#initialise some lists to hold the columns in the csv to easier analyse
candidate = []
u_candidate = []
u_count = []

#initialise a variable to hold the total number of votes
vote_count = 0


#open the csv file
with open(pypoll_src_path) as pypoll_src_csv:

    
    #read the csv file in python
    pypoll_read_csv = csv.reader(pypoll_src_csv, delimiter=',')

    
    #Skip the header row of the csv
    header = next(pypoll_read_csv)
    
    #loop through each row in the csv
    for row in pypoll_read_csv:
        #as each row is equal to a vote, our total number of votes is equal to the total number of rows, therefore...
        vote_count+=1
        
        #only storing candidate values in a table as they are the only thing we are performing analysis on
        candidate.append(row[2])

    #open a for loop to find unique candidates in the dataset
    for i in candidate:
        
        #set a condition that if the name that is being read in the loop is not in the unique names list, to store the new name in the list
        if i not in u_candidate:
            u_candidate.append(i)
            u_count.append(i) #ensure there is the same amount of items in the count list as there is in the unique candidate list

    #open a for loop that counts the amount of votes against the unique name that is being read by the loop
    for i in u_candidate:
        u_count[u_candidate.index(i)] = candidate.count(i)

        
#set a winners name by calling the index in the names list that matches the index which count value is the largest
winner = u_candidate[u_count.index(max(u_count))]

#print results in the terminal
print("Election Results")
print("-------------------------")
print(f"Total votes: {vote_count}")
print("-------------------------")

for i in u_candidate:
    print(f"{i}: {u_count[u_candidate.index(i)]/vote_count*100:.3f}% votes ({u_count[u_candidate.index(i)]})") #calculation for % of the vote is calculated in this function (i.e. count/total*100, for each name)

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#output to put into the txt file
#as the beginning and end of the file is static, while the middle loops, we can set two lists that are static and one that loops through the different values
output1 = ["Election Results\n",
            "----------------------------\n",
            f"Total votes: {vote_count}\n",
            "-------------------------\n"]

outputloop = []
for i in u_candidate:
    outputloop.append(f"{i}: {u_count[u_candidate.index(i)]/vote_count*100:.3f}% votes ({u_count[u_candidate.index(i)]})\n")

output2 = ["----------------------------\n",
            f"Total votes: {vote_count}\n",
            "-------------------------\n"]


#write the txt file
PyPoll_analysis = open('Analysis/PyPoll-analysis.txt','w')
PyPoll_analysis.writelines(output1+outputloop+output2)