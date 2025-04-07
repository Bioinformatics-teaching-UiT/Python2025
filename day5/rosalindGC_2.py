import os


# Fourth task: Computing GC Content.

# Goal: Find the DNA-sequence with the highest GC content and return it with the FASTA code and the GC content on separate lines

# I stored the sample dataset in its own .txt file to make it more "realistic"

# Reading the file:
def readFASTA(fileName: str) -> dict: # Could use a filepath as input
    """
    Function to read in a FASTA file, and return a dictioinary of sequences
    
    :param fileName: str, path to file
    :returns seqs: dict, dictionary is of form {id, sequence} 
    """
    with open(fileName, "r") as file:
        seqs = {} # Storing the sequences in a dict
        currentSeq = "" # Temp container for the current seq
        currentId = "" # And ID
        for line in file:
            if line.startswith(">"):
                if currentSeq: # Checks if there already is a seq stored in currentSeq
                    seqs[currentId] = currentSeq # Saves the current sequence in dict
                    currentSeq = "" # Resets the container after operation
                currentId = line.strip() # Updates current ID and removes whitespace and >
            else:
                currentSeq += line.strip() # Adds the line in currentSeq
        # After the last line in the file. If-statement to save the last sequence in the dict
        if currentSeq:
            seqs[currentId] = currentSeq
    return seqs

# From the other task
def GCcontent(seq: str) -> float:
    Gs = seq.count("G")
    Cs = seq.count("C")
    GC = (Gs + Cs) / len(seq) * 100
    return GC

def findHighestGC(seqs):
    id = ""
    max = 0
    for seqID, seq in seqs.items(): # For each id and sequence (from dict created by readFASTA)
        currentGC = GCcontent(seq)
        if currentGC > max: # Updates both id and seq to the one with the highest GC content
            id = seqID
            max = currentGC
    return id, max

seqs = readFASTA("FASTAsample.txt")
id, max = findHighestGC(seqs)

print(id[1:])
print(round(max, 6))

# Looks good






    



















