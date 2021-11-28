#import required modules to read csv

import os
import csv

#define a path variable using os.path.join to allow for reading on different os
pybank_src_path = os.path.join(".","Resources","budget_data.csv")


#initialise some lists to hold the two columns to easier analyse
#pl_diff is to make finding the average in the differences easier to find
date = []
prof_loss = []
pl_diff = []


#initialise variables to store the results
total_months = 0
total_pl = 0
pl_ave = 0
greatest_inc = 0
greatest_dec = 0


#open the csv file
with open(pybank_src_path) as pybank_src_csv:

    
    #read the csv file in python
    pybank_read_csv = csv.reader(pybank_src_csv, delimiter=',')

    
    #Skip the header row of the csv
    header = next(pybank_read_csv)

    
    #run a loop through the csv to...
    for row in pybank_read_csv:
        
        #count each iteration of the loop, this will reflect the amount of months that are represented in the data
        total_months += 1

        
        #separate the two columns of the csv into lists, this will make it easier to check values
        date.append(row[0])
        prof_loss.append(int(row[1])) #use int to ensure that the correct data type is stored for numerical analysis


    total_pl = sum(prof_loss)
        
    #loop through the pro_loss list and calculate the difference between each month
    for i in range(1,len(prof_loss)):#start at index 1 so that we can perform the "i-1" comparison in the loop
        pl_diff.append(prof_loss[i]-prof_loss[i-1])
        
                  
    #with the list we can find the average by finding the sum of the list, then dividing it by the total values in the list, which can be found with the "len()" function
    pl_ave = round(sum(pl_diff)/len(pl_diff),2)

    
    #use "max()" and "min()" functions to find the greatest increase and decrease in the change set
    greatest_inc = max(pl_diff)
    greatest_dec = min(pl_diff)
    
    
    #to find the month we just have to find the corresponding value in the "date" list, we add 1 to accomodate the shorter list as 
    greatest_inc_month = date[pl_diff.index(greatest_inc)+1]
    greatest_dec_month = date[pl_diff.index(greatest_dec)+1]
    
    
    #output analysis in terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_pl}")
    print(f"Average Change: ${pl_ave}")
    print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")

    
    #output to put into the txt file
    output = ["Financial Analysis\n",
              "----------------------------\n",
              f"Total Months: {total_months}\n",
              f"Total: ${total_pl}\n",
              f"Average Change: ${pl_ave}\n",
              f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n",
              f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})\n"]
    
#write the txt file
PyBank_analysis = open('Analysis/PyBank-analysis.txt','w')
PyBank_analysis.writelines(output)
