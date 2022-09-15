# The data we need to retrieve
# 1. The total number of votes casts
# 2. A colplete lists of candidates who recieved votes
# 3. The percentage of votes each candidates won
# 4. The total number of votes each candidates won
# 5. THE winner of the election based on popular vote

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
     #print(election_data)

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources" , "election_results.csv")

## Open the election results and read the file
with open(file_to_load) as election_data:

    # Print the file object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_load) as election_data:

  # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    print(headers)


