# election_analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of the recent local congressional election.  

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes ache candidate received.
4. Percentage of votes each candidate won.
5. The winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python v. 3.7, Visual Studio Code, v. 1.69.1

## Election Audit Results
The analysys of the election shows:
- There were 369,711 votes cast in the election
- Voter Turnout by County:
	- Jefferson County had 10.5% voter turnout and 38,855 number of votes
	- Denver County had 82.8% voter turnout and 306,055 number of votes
	- Arapahoe County had 6.7% voter turnout and 24,801 number of votes
-Largest County Turnout:
	- Denver county represented 82.8% of the total voter turn out, represnting 306,055 voters.
- The Candidates:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The Candidate Results:
	- Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
	- Diana DeGette received 73.8% of the votes and 272,892 number of votes.
	- Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
- The Election Winner:
	- Diana DeGette, who received 73.8% of the votes and 272,892 number of votes.

An image of the terminal results:

![code output](/resources/election_analysis.png)


## Election Audit Summary
The added requests for voter and county turnout is a good example of how this script can be modified. Voter turn out is important information to have for future elections. For example, it could influence resource allocations to boost areas of low turnout.

The script imports and reads a csv file containing voter results in three different counties. the fields inlcuded are: Ballot id, County, Candidate voted for. It then analyzes the data and creates a text file for documentation. The script defines and calcuates how many votes each candidate received. The script uses the same format to define and caluate the county turnout.

I propose this script be used for other elections.  The code provided is a very good tool for counting and auditing many types of elections and can be used on a much wider scale. For this election audit, the data provided  inlcuded three ccounties. Without editing the code, it could analyze all of the counties in Colorado by using an expanded dataset. This script can also be modified. It can easily be tailored to analyze state elections or evaluate different voter information if provided in the csv file.
