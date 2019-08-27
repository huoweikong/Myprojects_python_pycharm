# 改变大小写：
# Python 字符串具有很有用的转换大小写的 upper 和 lower 方法。
# 从 Biopython 1.53 起，Seq 对象也 获取了类似的方法应用于
# 字母表。例如:

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Alphabet import IUPAC


dna_seq = Seq("acgtACGT", generic_dna)
print(dna_seq)
print(dna_seq.upper())
print(dna_seq.lower())
print("GTAC" in dna_seq)
print("GTAC" in dna_seq.upper())
dna_seq = Seq("ACGT", IUPAC.unambiguous_dna)
print(dna_seq)

# 互补
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
print("原序列:\t\t\t", my_seq)
c = my_seq.complement()
print("互补:\t\t\t", c)
rc = my_seq.reverse_complement()
print("反向互补：\t\t", rc)
s = my_seq[::-1]
print("倒着读（3‘-5‘）：\t", s)

# 转录
print("\n转录部分：")
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
print("编码链：\t", coding_dna)
template_dna = coding_dna.reverse_complement()
print("模板链：\t", template_dna)
messenger_rna = coding_dna.transcribe()  #  mRNA
print("转录后:\t", messenger_rna)
coding_dna_back = messenger_rna.back_transcribe()
print("反转录：\t", coding_dna_back)

# 翻译
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)
print(messenger_rna)
post_translate = messenger_rna.translate()
print(post_translate)
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
post_translate2 = coding_dna.translate()
print(post_translate2)

# 翻译表
from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(standard_table)
print(mito_table)
print(mito_table.stop_codons)
print(mito_table.start_codons)
print(mito_table.forward_table["ACG"])

# 序列比对

seq1 = Seq("ACGT", IUPAC.unambiguous_dna)

seq2 = Seq("ACGT", IUPAC.unambiguous_dna)

my_seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)

#你可以使用 MutableSeq 对象将它转换成可变的序列，然后做任何你想要做的。
mutable_seq = my_seq.tomutable()
print(mutable_seq)

# 或者你可以直接从字符串建立一个 MutableSeq 对象：
from Bio.Seq import MutableSeq
mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)
print(mutable_seq)
mutable_seq[5] = 'C'
print(mutable_seq)
mutable_seq.remove('T')
print(mutable_seq)
print(type(mutable_seq))
new_seq = mutable_seq.toseq()
print(new_seq)
print(type(new_seq))

# 你可以使用所有常规的 Seq 对象，记住这些可以节省内存的 UnknownSeq 对象，如你所希望的那样在恰 当的地方使用。
from Bio.Seq import UnknownSeq

unk_dna = UnknownSeq(20, alphabet=IUPAC.ambiguous_dna)
print(unk_dna)
