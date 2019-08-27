from Bio import SeqIO

orchid_dict = SeqIO.to_dict(SeqIO.parse("sequence.fasta", "fasta"))
print(len(orchid_dict))
print(orchid_dict.keys())

print(orchid_dict.values())
seq_record = orchid_dict["KY624222.1"]
print(seq_record.description)
print(repr(seq_record.seq))
print(len(seq_record.seq))
