
#含有多个序列信息 将数据保存在字典中，键为基因名，值为基因序列

f = open('/home/miaoyr/perl_practice/test4_file/3.fasta_seq.txt')
seq = {}
for line in f:
        if line.startswith('>'):
                name=line.replace('>', '').split()[0]
                seq[name] = ''
        else:
                seq[name] += line.replace('\n', '').strip()
f.close()
