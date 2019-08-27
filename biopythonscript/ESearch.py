from Bio import Entrez
Entrez.email = "A.N.Other@example.com"
handle = Entrez.esearch(db="pubmed", term="biopython")
record = Entrez.read(handle)
print(record["IdList"])