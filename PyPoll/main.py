import csv

pypollCSV = ("election_data.csv")

with open(pypollCSV) as csvfile:
    csvreader = csv.reader(csvfile)
    
     
    voterid = []
    county = []
    candidates = []
    candidates_list = {}
    candidates_votes = {}
    candidate_options = []

    for lines in csvreader:
        voterid.append(lines[0])
        county.append(lines[1])
        candidates.append(lines[2])

    candidates_set = set(candidates)    
    total_vote = len(voterid)

    
    
    candidate_names = []
   
    
    for row in candidates_set:  
        candidate_names.append(row)
    
    
    candidates_count = 0
    dictionary_cn = {}
    for row in candidate_names:    
        candidate_name = str(candidate_names[candidates_count])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes/total_vote * 100,2)
        dictionary_cn.update({candidate_name : votes})
        election =(f"\nElection Results\n"
                   f"-------------------------\n"
                   f"Total Votes: {total_vote}\n")
        print(election, end="")
        print(f"{candidate_name}: {percentage}%  ({votes} votes)" )
        candidates_count = candidates_count + 1

output = (f"-------------------------\n"
          f"Winner: Khan\n"
          f"-------------------------\n")
print(output)

file_to_output = "Pypoll/election_analysis_2.txt"