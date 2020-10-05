# Election Analysis

## Overview of Election Audit
The purpose of the project was to conduct an audit of a  recent local congressional election. The election commission requested the following information:
* Who won the election.
* The total number of votes received.
* For each candidate, the number of votes received and the percentage of the total.
* Information about each county:
     - The county with the largest turnout.
     - The number of votes cast in each county.
	- Each county's vote percentage in comparison to the total votes cast.
	

To do this, I used Python. My input file was a CSV file containing ballot ID, county, and candidate.
## Election Audit Results
Here is the analysis of the election:
- **How many votes were cast in the congressional election?** There were 369,711 total votes cast in the election. 
- **County breakdown**:
  - Denver County received 306,055 votes or 82.8% of the total.
  - Jefferson County received 38,855 votes or 10.5% of the total
  - Arapahoe County received 24,801 votes or 6.7% of the total.
- 	**Which county had the largest number of votes?** Denver County had the largest number of votes.
- **Candidate breakdown**:
  - 1st place went to Diana DeGette, who received 272,892 votes or 73.8% of the total votes cast.
  - 2nd place went to Charles Casper Stockham, who received 85,213 votes or 23.0% of the total votes cast.
  - 3rd place went to Raymon Anthony Doane, who received 11,606 votes or 3.1% of the total votes cast.
- 	**Which candidate won the election, and what were his/her statistics?**  Diana DeGette, who received a total of 272,892 votes or 73.8% of the votes cast.

To get this information, I used:

* **Lists and dictionaries** to create the county and candidate lists. For example:

`county_options = []`
`county_votes_dict = {}`

* **"For" loops or repetition statements** to loop through each line of the CSV file. For example:

`for county_name in county_votes_dict:`
* **"If" or decision (conditional) statements** with logical operators. For example:

`if (votes > winning_county_count):`
* **CSV and OS modules** for the print statements to write to the screen and the file. For example:

`file_to_load = os.path.join('Resources\election_results.csv')`
`file_to_save = os.path.join("analysis", "election_results.txt")`

Here is a screenshot of the terminal showing these results:

![](./Resources/election_results.png)  

These results are also written to  /analysis/election_results.txt.

## Election Audit Summary
To summarize, this script worked well for its purpose and can be re-used, with some modifications, for any election. 

In the future, it can be modified in these ways:
- It can show the winner in each county.
- It can show the candidate breakdown by county, showing the number of votes each candidate received and the percentage of total votes received in that county.



