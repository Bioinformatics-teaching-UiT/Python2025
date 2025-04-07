sequences = {}



with open("Rosalind_GC.txt","r") as Rosa:
    header = ""
    sequence = ""
    for line in Rosa:
        print(line)
        line = line.strip()
        if line.startswith(">"):
            sequence = ""
            header = line[1:-1]
            print(header)
        else:
            sequence += line.strip()
            sequences[header] = sequence



gc_content=0

for key in sequences:
    gc_count = 0
    for base in sequences[key]:
        gc_count = sequences[key].count("G") + sequences[key].count("C")
    if gc_content < gc_count/len(sequences[key]):
        gc_content = gc_count/len(sequences[key])
        gc_key=key

print(gc_key)
print(gc_content)


