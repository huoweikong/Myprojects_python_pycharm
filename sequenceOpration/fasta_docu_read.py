#只含一个基因序列将FASTA文件的基因序列读取到一个列表中，列表中的每个元素为每一行基因序列构成的字符串


f = open('/home/miaoyr/perl_practice/test1_file/DTNBP1.fasta')
ls=[]
for line in f:
    if not line.startswith('>'):
        ls.append(line.replace('\n', ''))#去掉行尾的换行符真的很重要！  
f.close()
