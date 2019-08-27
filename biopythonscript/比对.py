from Bio.Align.Applications import ClustalwCommandline
clustalw_exe = r"C:\Program Files\new clustal\clustalw2.exe"
#from StringIO import StringIO
from Bio import AlignIO
cline = ClustalwCommandline("clustalw2", infile="asfv_p72.fasta")
print(cline)
stdout, stderr = cline()
align = AlignIO.read(StringIO(stdout), "fasta")
print(align)