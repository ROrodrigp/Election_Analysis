#The data we need to retrieve
#1. The total number of votes cast 
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won 
#4. The total number of votes each candidate won 
#5. The winner of the election based on popular vote 

# Import the datetime class from the datetime module.
import datetime as dt 
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
import os 

#file_to_load = "Resources/election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Each row in the CSV file was printed out as a list.
    header = next(file_reader)
    print(header)

file_to_save = "Analysis/election_analysis.txt"
#outfile = open(file_to_save, "w")
#outfile.write("Hello world")
#outfile.close()
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Araphoe\nDenver\nJefferson")
