with open("..\\Datasets\\rosalind_dna.txt", "r") as file:
    dna_sequence = file.read().strip()

print(dna_sequence.count("A"), dna_sequence.count("C"), dna_sequence.count("G"), dna_sequence.count("T"))