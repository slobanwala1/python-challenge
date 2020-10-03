import os
import csv

# Path to collect data from the Resources folder

election_data_csv = os.path.join('..', 'PyPoll/Resources', 'election_data.csv')

# Use encoding or else it gives weird data

total_votes = 0
candidates = {}
winner = ''

with open(election_data_csv, newline="", encoding="utf-8") as csvfile:
    
    # Split the data on commas
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        
        # Count total votes
        
        total_votes += 1
        
        # Grab each candidate assuming we don't have a list to begin with
        
        if row[2] in candidates:
            candidates[row[2]] += 1 
        else:
            candidates[row[2]] = 1
            

        
# Get the winner

winner = max(candidates, key=candidates.get)

# Have the winner and each candidate with there votes and total votes so time to print.

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------')

# Print Candidates, Percentage of each votes candidate won, and total Candidate votes

for key, value in candidates.items():
    print(key + ': ' + '{:.3f}'.format(round((value/total_votes)*100,3)) + '% (' + str(value) + ')')
print('-------------------------')
print('Winner: ' + winner)
print('-------------------------')
        
        
# Write output to file  


election_results = os.path.join('..', 'PyPoll/analysis', 'Election_results.txt')

file = open(election_results, 'w')

file.write('Election Results')
file.write('\n')
file.write('-------------------------')
file.write('\n')
file.write('Total Votes: ' + str(total_votes))
file.write('\n')
file.write('-------------------------')
file.write('\n')
for key, value in candidates.items():
    file.write(key + ': ' + '{:.3f}'.format(round((value/total_votes)*100,3)) + '% (' + str(value) + ')')
    file.write('\n')
file.write('-------------------------')
file.write('\n')
file.write('Winner: ' + winner)
file.write('\n')
file.write('-------------------------')
file.close()  