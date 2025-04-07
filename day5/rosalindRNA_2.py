
# Second task: Transcribing DNA into RNA

# Once again, we have done this before. 

# Sample data
seq = "GATGGAACTTGACTACGTAAATT"

mapping = {"G": "G", "C": "C", "T": "U", "A": "A"}

complementDNA = ""
for base in seq:
    complementDNA += mapping[base] # Adds the base to the complementDNA string
print(complementDNA)

# Looks like the sample output provided on the site. (This was an easier solution than what I had in the other task. Maybe I overcomplicated it?)


























