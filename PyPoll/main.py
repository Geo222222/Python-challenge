import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_votes = {}
candidates = []

with open(csv_path, 'r') as file:
    csv_read = csv.reader(file, delimiter=',')
    
    next(csv_read)
    
    for row in csv_read:
        total_votes += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidates:
            candidates.append(candidate_name)
        
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

percentages = {}
for candidate in candidate_votes:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    percentages[candidate] = percentage

winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_folder = os.path.join("..", "analysis")
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "election_results.txt")

with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
