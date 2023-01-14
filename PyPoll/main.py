import csv

# initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
winning_votes = 0

# open and read csv file
with open("Resources/election_data.csv", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip header row
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        # add candidate to dictionary if not already in there
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        # increment candidate's vote count
        candidate_votes[candidate] += 1

# print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# iterate through candidates and their votes
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# export results to text file
with open("analysis/output.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")