# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

#import csv
#dir(csv)

# Assign a variable for the file to load and the path. - this works
#file_to_load = 'Resources\election_results.csv'

# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
   #  print(election_data)

#===============
#Add our dependencies
import csv
import os
#print(dir(os))
#dir(os.path)

# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Amy Tieku", "ELECTION ANALYSIS", "Resources", "election_results.csv")
file_to_load = 'Resources\election_results.csv'

# Create a filename variable to a direct or indirect path to the file.
file_to_save = 'analysis\election_analysis.txt'

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
       # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    #print(headers)
      # Print each row in the CSV file.
    #on 10/2
    for row in file_reader:
           # 2. Add to the total vote count.
        total_votes += 1

          # Print the candidate name from each row.
        candidate_name = row[2]

   # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
     # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
       # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

  # Determine the percentage of votes for each candidate by looping through the counts.
  # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
      # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    
      # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

          # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
      #  To do: print out the winning candidate, vote count and percentage to
  #   terminal.
      #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

  # Determine winning vote count and candidate
  # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
      # 2. If true then set winning_count = votes and winning_percent =
      # vote_percentage.
           winning_count = votes
           winning_candidate = candidate_name
           winning_percentage = vote_percentage
      # 3. Set the winning_candidate equal to the candidate's name.
      

      # 4. Print the candidate name and percentage of votes.
      #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")  

  #Print the winning candidates' results to the terminal.

    winning_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"-------------------------\n")


    print(winning_candidate_summary)
     # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    # Add the candidate name to the candidate list.
        # candidate_options.append(candidate_name)

        #  print(row)
  # 3. Print the total votes.
  #print(total_votes)

      # Print the file object.
    #print(election_data)
  # Print the candidate list.
  #print(candidate_votes)

  # Using the open() function with the "w" mode we will write data to the file.
  #outfile = open(file_to_save, "w")
  #with open(file_to_save, "w") as txt_file:
  # Write some data to the file.
  #outfile.write("Hello World")
    #txt_file.write("Hello Wonderful World")

      # Write three counties to the file.
    #  txt_file.write("Counties in the election\n")
      # txt_file.write("---------------------\n")
      # txt_file.write("Arapahoe\nDenver\nJefferson")
  # Close the file
  #outfile.close()