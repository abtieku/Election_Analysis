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
# Open the election results and read the file.
with open(file_to_load) as election_data:
       # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
      # Print each row in the CSV file.
    #on 10/2
    #for row in file_reader:
    #    print(row)

    # Print the file object.
   #print(election_data)


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