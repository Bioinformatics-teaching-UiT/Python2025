
sequences = {}

with open("Rosalind_GC_1.txt","r") as Rosa:
    header = ""
    sequence = ""
    for line in Rosa:
        line = line.strip()
        if line.startswith(">"):
            if header:
                sequences[header] = sequence
            header = line[1:]
            sequence = ""
        else:
            sequence += line
            sequences[header] = sequence

outputfile = open("Rosalind_GC_output.txt","w")

for key in sequences:
    print(outputfile.write(key+"\t"+sequences[key]+"\n"))

outputfile.close()