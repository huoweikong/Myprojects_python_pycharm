from Bio import  AlignIO
import Bio.Align.Applications

print(dir(Bio.Align.Applications))



'''
alignments = AlignIO.parse("sequence.fasta","fasta")
for alignment in alignments:
    print(alignment)
    print()
'''