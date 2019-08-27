from Bio import Entrez
from Bio import SeqIO
Entrez.email = "A.N.Other@example.com"
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", \
                       id="6273291,6273290,6273289")
for seq_record in SeqIO.parse(handle, "gb"):

    print(seq_record.id, seq_record.description[:50] + "...")

    print("Sequence length %i," % len(seq_record),)

    print("%i features," % len(seq_record.features))

    print("from: %s" % seq_record.annotations["source"])

handle.close()
