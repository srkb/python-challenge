import os
import csv

pypoll_election_data = os.path.join("/Users/3544000/workspace2/dataAnalytics/python-challenge/PyPoll/Resources/election_data.csv")

with open(pypoll_election_data, newline="") as election_data_file:
    csvreader = csv.reader(election_data_file, delimiter=",")

    election_data_file_header = next(csvreader)

    total_votes=0
    candidate_votes_dict = {}

    for row in csvreader:

        total_votes += 1
        candidate = row[2]
        if candidate not in candidate_votes_dict:
            candidate_votes_dict[candidate] = 1
        else:
            candidate_votes_dict[candidate] +=1

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for key, value in candidate_votes_dict.items():
    print(f"{key}: {(value / total_votes):.3%} ({value})")
print(f"-------------------------")
print(f"Winner: {max(candidate_votes_dict, key=candidate_votes_dict.get)}")
print(f"-------------------------")              


output_file = os.path.join('/Users/3544000/workspace2/dataAnalytics/python-challenge/PyPoll/analysis', 'pyPoll_output.txt')

pyPollAnalysis = open(output_file, "w")

lines =[]
lines.append("Election Results\n")
lines.append("----------------------------\n")
lines.append(f"Total Votes: {total_votes}\n")
lines.append(f"-------------------------\n")
for key, value in candidate_votes_dict.items():
    lines.append (f"{key}: {(value / total_votes):.3%} ({value})\n")
lines.append(f"-------------------------\n")
lines.append(f"Winner: {max(candidate_votes_dict, key=candidate_votes_dict.get)}\n")
lines.append(f"-------------------------")
pyPollAnalysis.writelines(lines)
pyPollAnalysis.close  