from Bio import SeqIO

orchid_dict = SeqIO.index("sequence.fasta", "fasta")
print(len(orchid_dict))
print(orchid_dict.keys())
seq_record = orchid_dict["KY624222.1"]
print(seq_record.description)
print(seq_record.seq)