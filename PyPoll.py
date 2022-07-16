
    ## ADD Dependancies
import csv
import os

    ## Assign a variable to LOAD a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

    ## Assign a variable to SAVE the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

    ## Open the election results and read the file.
with open(file_to_load) as election_data:

        ## To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
        ## Print each row in the CSV file.
    # for row in file_reader:  
    #     print(row)

        ## Read and print the header row.
    headers = next(file_reader)
    print(headers)

# #------------------------------------
# # Total number of votes cast
# # A complete list of candidates who received votes
# # Total number of votes each candidate received
# # Percentage of votes each candidate won
# # The winner of the election based on popular vote