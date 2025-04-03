"""
Calculate the GC content of the following sequences:
"""

sequence1 = 'GCGATACGTCGCGCTAGGGCCCATATTATAACGCGCTAGGCTATCGATTTATATATCGCGCGCGGGGGGCCAATATAAAAATCCCATTCCGGGG'
sequence2 = 'ATATAAAACCCGGGGAACGATTATCGACGCCGACTACACTACGATCGAGCGATCATTATATCGCAACACACAATATAAAAAAATTTCGCGC'
sequence3 = 'ATATATATTTTATTATATTTATATATTATATATATTATAAAAAAAAAAATTTATATATATAT'
sequence4 = 'GGGGGGGGGGCCGCCCCCCCCCGCGGCCCCCCCCCCCCCCGCGCGCGGGGGCGGCGCGGGGGGCCC'

# Using the formula: (number of G + number of C) / seq-length (times 100 if you like, I don't)

def GCcontent(seq: str) -> float: # Strings only!
    Gs = seq.count("G")
    Cs = seq.count("C")
    GC = (Gs + Cs) / len(seq)
    return GC

sequences = [sequence1, sequence2, sequence3, sequence4]  

for seq in sequences:
    print(GCcontent(seq)) # Easy to append and store in list if preferable

# Looks correct. 0 and 1 for the third and fourth sequences