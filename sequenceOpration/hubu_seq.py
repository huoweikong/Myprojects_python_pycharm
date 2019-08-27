#输出互补序列：
#f = open('/home/miaoyr/perl_practice/test4_file/3.fasta_seq.txt')
f = open("/Users/aiqiangyun/Desktop/实验相关/实验材料及方法/WHC27505  (WHC27505-人源IgG-Fc)/S25070-G128187-1  _M13-77-E11.seq")
seq = {}
complement = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A', '\n': '\n'}
for line in f:
        if line.startswith('>'):
                name = line
                seq[name] = ''
        else:
                line = line.lstrip()
                for i in line:
                        seq[name] += complement[i]#将互补序列存储到字典的值中
f.close()
_str = []
l = open('4-5-output.txt', 'w')
for key in seq.keys():#按fasta文件格式输出
        _str.append("%s%s\n" % (key, seq[key]))
l.writelines(_str)
l.close()
