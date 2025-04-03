"""
1. Do the following sequences of DNA contain the pieces given after them?
If so, how many times?

2. Then, count in total how many times A, T, C, G occur, using a dictionary and one loop only.

3. Transcribe this sequence to RNA.

Bonus:
    Complement this strand of DNA using a list comprehension. Then transcribe that complemented strain.
"""

### 1

sequence_1 = """AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGT
	GGATTAAAAAAAGAGTGTCTGATAGCAGCAGCTTTTCATTCTGACTGCAA
        CGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCACGATGTCGGATCGTAT
	GCTAGTCAGTGTGTTTTTTTTAAAAGCAGGCTGCATGCTGTGTGTGTGTACGTATATGAAAAAATCAGC"""

piece_1_1 = 'GCA'
piece_1_2 = 'ATT'
piece_1_3 = 'TCA'
piece_1_4 = 'GCAAATCC'

print(sequence_1) # Needs some cleaning

sequence_1 = sequence_1.replace("\n", "") # All in one line
print(sequence_1)

# 1. --- Next step: Check for parts ---
pieces = [piece_1_1, piece_1_2, piece_1_3, piece_1_4]

piecesOccur = {}
for piece in pieces:
    piecesOccur[piece] = sequence_1.count(piece)
    
print(piecesOccur) # Good

# --- 2. Next step: Count how many times A, T, C, G occurs ---
# A dict with counts initialized as zero
nuclearOccur = {"A": 0, "T": 0, "C": 0, "G": 0}
for nuke in sequence_1:
    if nuke in nuclearOccur:
        nuclearOccur[nuke] += 1
print(nuclearOccur) # Looks right

# --- 3. Next step: Transcript to RNA ---
mapping = {"G": "C", "C": "G", "T": "A", "A": "T"}

# To remove the tab and blank spaces. The sequence can only contain bases in the mapping. else: KeyError
sequence_1 = sequence_1.replace("\t", "").replace(" ", "")

complementDNA = ""
for base in sequence_1:
    complementDNA += mapping[base] # Adds the base to the complementDNA string
print(complementDNA)

complementRNA = ""
for base in complementDNA:
    if base == "T":
        complementRNA += "U"
    else:
        complementRNA += base

print(complementRNA) # Looks good





