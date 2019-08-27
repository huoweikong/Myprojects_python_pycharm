from Bio import Entrez
from Bio import SeqIO
import os

Entrez.email = "A.N.Other@example.com"
filename = "gi_186972395.gbk"
if not os.path.isfile(filename):
    net_handle = Entrez.efetch(db="nucleotide", id="186972394",
                       rettype="gb", retmode="text")
    out_handle = open(filename, "w")

    out_handle.write(net_handle.read())
    out_handle.close()
    net_handle.close()
    print("saved")
else:
    print("this file has solved")

print("Parsing...")
record = SeqIO.read(filename, "genbank")
print(record)

#为了得到 XML 格式的输出，你可以使用 Bio.Entrez.read() 函数和参数 retmode="xml" 进行解析，：
handle = Entrez.efetch(db="nucleotide", id="186972394", retmode="xml")
record = Entrez.read(handle)
handle.close()
print(record[0]["GBSeq_definition"])
print(record[0]["GBSeq_source"])


'''

handle = Entrez.efetch(db="nucleotide", id="186972394",
                       rettype="gb", retmode="text")

print(handle)


record = SeqIO.read(handle, "genbank")
handle.close()
print(record)
'''