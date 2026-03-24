with open("..\\Datasets\\rosalind_rna.txt", "r") as f:
    file = f.read().strip()
    rna = file.replace("T", "U")
    print(rna)