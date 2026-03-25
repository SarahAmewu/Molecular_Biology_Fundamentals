with open("..\\Datasets\complement_rev.txt", "r") as f:
    file = f.read().strip()
table = str.maketrans("ATCG", "TAGC")
complement = file.translate(table)
reverse = complement[::-1]
print(reverse)