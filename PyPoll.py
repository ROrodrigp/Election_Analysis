#The data we need to retrieve
#1. The total number of votes cast 
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won 
#4. The total number of votes each candidate won 
#5. The winner of the election based on popular vote 

# Import the datetime class from the datetime module.
import datetime as dt 
import csv
import os 
# Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)


#file_to_load = "Resources/election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = "Analysis/election_analysis.txt"
total_votes = 0 
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Each row in the CSV file was printed out as a list.
    header = next(file_reader)
    # print(f'The headers are {header}')

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name]+= 1
    # print(total_votes)
    # print(candidate_options)
    # print(candidate_votes)

with open(file_to_save, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f'Total Votes: {total_votes:,}\n')
    txt_file.write("-------------------------\n")


    for candidate in candidate_options:
        
        votes_percentages = float(candidate_votes[candidate]) / float(total_votes) * 100 
        # print(f'{candidate}: received {votes_percentages:.1f}% and {candidate_votes[candidate]:,} votes')
        candidate_results = (f'{candidate}: received {votes_percentages:.1f}% and {candidate_votes[candidate]:,} votes\n')
        txt_file.write(candidate_results)
        
        if (candidate_votes[candidate] > winning_count) and (votes_percentages > winning_percentage):
            winning_count = candidate_votes[candidate]
            winning_percentage = votes_percentages
            winning_candidate = candidate
    txt_file.write("-------------------------\n")
    winning_candidate_summary = (
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count {winning_count:,}\n'
        f'Winning Percentage {winning_percentage:.1f}%\n'
        f'-------------------------\n'
    )
    txt_file.write(winning_candidate_summary)

# print(winning_candidate_summary)

#outfile = open(file_to_save, "w")
#outfile.write("Hello world")
#outfile.close()
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the election\n")
#     txt_file.write("--------------------------\n")
#     txt_file.write("Araphoe\nDenver\nJefferson")
