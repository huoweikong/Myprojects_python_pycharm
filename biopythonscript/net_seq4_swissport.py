#解析来自网络的 SwissProt 序列条目

#现在我们使用句柄下载来自 ExPASy 的 SwissProt 文件，
# 更深入的信息请见第10 章。如上面提到的， 当你希望处理的对象包
# 含有且仅有一条序列条目时，使用 Bio.SeqIO.read() 函数：

from Bio import ExPASy
from Bio import SeqIO
handle = ExPASy.get_sprot_raw("O23729")
seq_record = SeqIO.read(handle, "swiss")
handle.close()
print(seq_record.id)
print(seq_record.name)
print(seq_record.description)
print(repr(seq_record.seq))
print("Length %i" % len(seq_record))
print(seq_record.annotations["keywords"])