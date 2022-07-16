
    ## ADD Dependancies
import csv
import os

    ## Assign a variable to LOAD a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
    ## Assign a variable to SAVE the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")



    ## Initiallize a TOTAL VOTES counter
total_votes = 0

    ## Candidate Options & Votes - declare an empty lists
candidate_options = []
    ## Declare empty dict
candidate_votes = {}

    ## Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0



    ## Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

        ## Read the header row.
    headers = next(file_reader)

        ## PRINT each row in the CSV file.
    for row in file_reader:

            ## 2. Add to the TOTAL VOTES count.
        total_votes += 1

            ## Print the CANDIDATE NAME from each row
        candidate_name = row[2]

        ## If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
                ## Add it to the list of candidates.
            candidate_options.append(candidate_name)
                ## Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

            ## Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        ## Determine the percentage of votes for each candidate by looping through the counts.

#save results to text file
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


        ## Iterate through the candidate list.
    for candidate_name in candidate_votes:
            ## Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
            ## Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

            ## declase the print variable
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            ## print to terminal
        print(candidate_results)
            ## print to text file
        txt_file.write(candidate_results)


        ### Determine winning vote count and candidate
            ## Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
    
        ##Print to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        ##print to text file
    txt_file.write(winning_candidate_summary)




# #------------------------------------
# # Total number of votes cast
###     369711
# # A complete list of candidates who received votes
###     ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
# # Total number of votes each candidate received
###     {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
# # Percentage of votes each candidate won
###     Charles Casper Stockham: received 23.0% of the vote.
###     Diana DeGette: received 73.8% of the vote.
###     Raymon Anthony Doane: received 3.1% of the vote.
# # The winner of the election based on popular vote
###     -------------------------
###     Winner: Diana DeGette
###     Winning Vote Count: 272,892
###     Winning Percentage: 73.8%
###     -------------------------