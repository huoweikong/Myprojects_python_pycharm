
#碱基数目和序列长度统计：
#上一步将基因序列写入列表，为了使用str.count()函数（使用对象为字符串）直接计算，将全部基因序列合并为一个字符串_str

#f=open('/home/miaoyr/perl_practice/test1_file/DTNBP1.fasta')
f = open('/Users/aiqiangyun/Desktop/实验相关/实验材料及方法/WHC27505  (WHC27505-人源IgG-Fc)/S25070-G128187-1  _M13-77-E11.seq')
ls = []
for line in f:
        if not line.startswith('>'):
                ls.append(line.replace('\n', ''))#去掉行尾的换行符真的很重要!
f.close()


A = C = T = G = 0
_str = ''
for i in range(0, len(ls)):
        _str += ls[i]
print(_str)
A += _str.count('A')
C += _str.count('C')
T += _str.count('T')
G += _str.count('G')
print('A:', A, '\n', 'C:', C, '\n', 'T:', T, '\n', 'G:', G, '\n')
length = A + T + C + G
print("A+T+C+G为:", length)
