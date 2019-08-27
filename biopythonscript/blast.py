from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")

#fasta_string = open("m_cold.fasta").read()
#result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

#from Bio import SeqIO
#record = SeqIO.read("m_cold.fasta", format="fasta")
#result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)

save_file = open("my_blast.xml", "w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
result_handle = open("my_blast.xml")

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)
print(blast_record)
