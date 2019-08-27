from Bio import SeqIO
records = list(SeqIO.parse("sequence.fasta", "fasta"))

print("Found %i records" % len(records))

print("The last record")
last_record = records[-1] #using Python's list tricks
print(last_record.id)
print(repr(last_record.seq) )
print(len(last_record))

print("The first record")
first_record = records[0] #remember, Python counts from zero
print(first_record.id)
print(repr(first_record.seq))
print(len(first_record))

'''
records = dict(SeqIO.parse("sequence.fasta", "fasta"))
print(records.annotations)
print(first_record.annotations.keys())
print(first_record.annotations.values())
'''