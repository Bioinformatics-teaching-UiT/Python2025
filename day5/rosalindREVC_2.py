
# Third task: Complementing a Strand of DNA

# Sample sequence
seq = "AAAACCCGGT"

mapping = {"G": "C", "C": "G", "T": "A", "A": "T"}

reverseComplementDNA = ""
for base in seq[::-1]:
    reverseComplementDNA += mapping[base]
    
print(reverseComplementDNA) # Looks good





















